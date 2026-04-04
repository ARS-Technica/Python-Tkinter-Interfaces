"""
Search Widgets Across Files 
Author: Andrew R Sutton
Created: March 23, 2026

The purpose of this project is to demonstrate how to 
search text in a tkinter text widget from another Python 
file inside the same project?

In short, this is an exercise in how to keep projects 
appropriately modular.

This project was inspired by the following Stack Overflow threads:

"How can you use tkinter widgets across files in python?"
https://stackoverflow.com/questions/55445332/how-can-you-use-tkinter-widgets-across-files-in-python

"Insert text via pythons .insert() method to a tkinter Text() widget that resides in another file"
https://stackoverflow.com/questions/71490449/insert-text-via-pythons-insert-method-to-a-tkinter-text-widget-that-resides

Lessons learned from this project will eventually be implimented in 
my larger Advanced Text Editor project, which is currently a single 
enormous tangle of code housed inside a single file.
"""

"""
Goals:
To search text in a Tkinter Text widget from another Python file, you must pass the widget object as an argument to the function defined in the external file.  Since Python modules cannot directly access variables from the file that imports them, you must explicitly pass the widget object via function parameters.

1. Create the Search Function (search_logic.py) 
Define a function that takes the Text widget and the search string as parameters. Use the search() method on the passed widget.

2. Implement the GUI (main.py) 
Import the search function and pass your local Text widget instance to it when a button is clicked.
"""

from logging import root
import tkinter as tk
from tkinter import messagebox
import search_logic

# Table of Contents
    # Constants
    # Global Variables
    # Search Function
    # Search Helper Functions
    # User Interface
    # Key Bindings


# CONSTANTS ------------------------------------------------------------------------------

# Search results highlighting configurations.  Adjusts the visual style of search results. 
HIGHLIGHTING_CONFIGURATIONS = {
    "active": {"background": "blue",   "foreground": "white"},
    "error":  {"background": "red",    "foreground": "white"},
    "found":  {"background": "yellow", "foreground": "black"},
    "next":   {"background": "orange", "foreground": "black"}    
}


# GLOBAL VARIABLES ------------------------------------------------------------------------

# Declare variables for UI elements as None
search_entry = None
status_label = None
text_area = None


# SEARCH FUNCTION -------------------------------------------------------------------------

def on_search_click():
    """
    Connects the GUI in main.py to the search logic in search_logic.py

    Triggered when the user clicks "Search" or presses the Enter key.  This function
    pulls the string from the Entry widget, calls find_all() from the logic file, and 
    updates a status label.
    
    1. Input Validation: Ensures the user provided a search term.
    2. Data Retrieval: Pulls the current state from the GUI (search_entry).
    3. External Execution: Passes the local widget instance to external search_logic.find_all
    4. UI Feedback: Interprets the results and updates the Status Bar for the user.
    """

    # Step 1: Data Retrieval
    # Pull the string currently typed in the Entry widget.
    query = search_entry.get()
    
    # Variable for the tag name to avoid hardcoding strings in the logic call
    target_tag = "found"     

    # Step 2: Input Validation (Guard Clause)
    # If the user clicks search with an empty box, stop early to save resources
    if not query:
        update_status("Error: Please enter a search term.", "red")
        return

    try:
        # Step 3: Dependency Injection (The Core of the Project)
        # Pass the local 'text_area' (a widget instance) and the 'query' 
        # to the find_all function defined in search_logic.py.
        match_count = search_logic.find_all(text_area, query, tag_name=target_tag)

        # Step 4: Conditional UI Update
        # Update the status bar with the integer returned from the logic file.
        if match_count and match_count > 0:
            update_status(f"Success: Found {match_count} matches.")        

            # Step 5: UX Enhancement
            # Scroll the first occurrence of the 'found' tag into the user's view.
            text_area.see(f"{target_tag}.first")
        else:
            update_status("Search complete: No matches found.", "blue")

    except Exception as e:
        # Step 6: Error Handling
        # If the widget instance is lost or corrupted, catch the error
        update_status("Technical Error: Search failed.", "red")
        print(f"Developer Debug Log: {e}")


# SEARCH HELPER FUNCTIONS ------------------------------------------------------------------

def define_highlights(text_widget, styles_dict):
    """
    Iterate through the style dictionary and configures the widget tags.
    Maximizes modularity by eliminating the need to define highlights inside search.
    """
    for tag, colors in styles_dict.items():
        text_widget.tag_config(tag, **colors)  


def on_clear_click():
    """
    Clears all highlights and empties the search box.
    Calls clear_tags() from the logic file and uses entry.delete(0, tk.END).
    """
    # Clear the UI entry box
    search_entry.delete(0, tk.END)

    try:
        # Call the logic function to wipe all tags from the text area 
        search_logic.clear_tags(text_area)
        # Provide user feedback
        status_label.config(text="Highlights successfully cleared.", fg="black")
    except AttributeError:
        status_label.config(text="Error: Could not access text area.", fg="red")


def update_status(message, color="black"):
    """
    Updates the status bar label with the number of search instances in the document
    "Found 3 matches" or "No results"
    """
    status_label.config(text=message, fg=color)


# USER INTERFACE  ------------------------------------------------------------------------

def build_user_interface(root):
    """
    Layout engine.  This function organizes the interface.
    Create the Text widget, the Entry field for searching, and the action buttons.
    Uses Frames to group the "Search Tools" at the top and text input below.
    """

    global search_entry, status_label, text_area

    # root = tk.Tk() # Moved to the if __name__ == "__main__": block at the bottom
    root.title("Modular Tkinter Search")

    # Search Control Panel (Header)
    header = tk.Frame(root)
    header.pack(pady=10, padx=10, fill='x')

    # Search Form
    search_entry = tk.Entry(header)
    search_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=5)
    search_entry.bind("<Return>", lambda e: on_search_click())    # Bind 'Enter' key

    tk.Button(header, text="Find All", command=on_search_click).pack(side=tk.LEFT, padx=2)
    tk.Button(header, text="Clear", command=on_clear_click).pack(side=tk.LEFT, padx=2)

    # Text Area (Body)
    text_area = tk.Text(root, wrap='word', height=15)
    text_area.pack(padx=10, pady=5, fill='both', expand=True)

    # Sample text for Text Area
    text_area.insert("1.0", "This project demonstrates how to search a Text Widget from another python file.\n\nTo search text in a tkinter Text Widget from another file, you must pass the widget instance as an argument to a function in the second file.\n\nIn this example, I am triggering the search logic in search_logic.py with the on_search_click function in main.py.")

    # Define the styles immediately after the text_area widget is created. 
    define_highlights(text_area, HIGHLIGHTING_CONFIGURATIONS)

    # Status Bar (Footer)    
    status_label = tk.Label(root, text="Ready", bd=1, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill='x', padx=(10, 0))


# KEY BINDINGS ---------------------------------------------------------------------------

# Binding
    # Bind the Return (Enter) key to the search function. 
    # Allows the user to type a word and just hit Enter instead of reaching for the mouse—a standard feature in any real-world text editor.


def on_key_release(event):
    """
    Example: Updates 'Matches Found' label in status bar.
    """

    query = search_entry.get()
    
    # We call the dry-run count function
    num_matches = search_logic.get_match_count(text_area, query)
    
    # Update the UI without actually highlighting anything yet
    match_label.config(text=f"Matches found: {num_matches}")


# MAIN EXECUTION ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Create the root before we build the UI
    main_window = tk.Tk()
    build_user_interface(main_window)
    main_window.mainloop()

