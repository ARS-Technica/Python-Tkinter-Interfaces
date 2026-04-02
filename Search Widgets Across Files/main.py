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

import tkinter as tk
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
    "active": ("blue", "white"),
	"error": ("red", "white"),
	"found": ("yellow", "black"),
	"next": ("orange", "black")    
    }


# GLOBAL VARIABLES ------------------------------------------------------------------------

# Declare variables for UI elements as None
search_entry = None
status_label = None
text_area = None


# SEARCH FUNCTION -------------------------------------------------------------------------


# SEARCH HELPER FUNCTIONS ------------------------------------------------------------------

def clear_highlights():
    """Resets all tags in the text widget in order to remove highlighting of text."""
    try:
        search_logic.clear_tags(text_area, tag_name="found")
        status_label.config(text="Highlights successfully cleared.", fg="black")
    except AttributeError:
        status_label.config(text="Error: Could not access text area.", fg="red")


def define_highlights(text_widget, styles_dict):
    """
    Iterate through the style dictionary and configures the widget tags.
    Maximizes modularity by eliminating the need to define highlights inside search.
    """
    for tag, colors in styles_dict.items():
        # **colors unpacks the dict into: background="yellow", foreground="black"
        text_widget.tag_config(tag, **colors)  

# apply_styles(text_area, HIGHLIGHTING_CONFIGURATIONS)


def on_search_click():
    """
    The 'Bridge' Controller: Orchestrates the search process between the UI and Logic.
    
    This function acts as the central coordinator. It performs the following roles:
    1. Input Validation: Ensures the user provided a search term.
    2. Data Retrieval: Pulls the current state from the GUI (search_entry).
    3. External Execution: Passes the local widget instance to the external 
       'search_logic' module.
    4. UI Feedback: Interprets the results and updates the Status Bar for the user.
    """

	# Step 1: Data Retrieval
	# Pull the string currently typed in the Entry widget.

	# Step 2: Input Validation (Guard Clause)
	# If the user clicks search with an empty box, stop early to save resources

	# Step 3: Dependency Injection (The Core of the Project)
	# Pass the local 'text_area' (a widget instance) and the 'query' 
	# to the find_all function defined in search_logic.py.

	# Step 4: Conditional UI Update
	# Update the status bar with the integer returned from the logic file.

	# Step 5: UX Enhancement
	# Scroll the first occurrence of the 'found' tag into the user's view.

	# Step 6: Error Handling
	# If the widget instance is lost or corrupted, catch the error 

    pass


def on_clear_click():
    """
    Clears all highlights and empties the search box.
    Calls clear_highlights() from the logic file and uses entry.delete(0, tk.END).
    """

    search_entry.delete(0, tk.END)
    search_logic.clear_tags(text_area, tag_name="found")
    update_status("Highlights successfully cleared.")


def update_status(message):
    """
    Updates the status bar label with the number of search instances in the document
    "Found 3 matches" or "No results"
    """

    status_label.config(text=message, fg="black")


# USER INTERFACE  ------------------------------------------------------------------------

def user_interface(root):
    # Layout engine.  This function organizes the interface.
    # Purpose: Create the Text widget, the Entry field for searching, and the action buttons.
    # Logic: Uses Frames to group the "Search Tools" at the top and text input below.

    global search_entry, status_label, text_area

    root = tk.Tk()
    root.title("Modular Tkinter Search")

    # Control Panel (Header)
    header = tk.Frame(root)
    header.pack(pady=10, padx=10, fill='x')

    # Search Form
    search_entry = tk.Entry(header)
    search_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=5)
    search_entry.bind("<Return>", lambda e: handle_search())    # Bind 'Enter' key

    btn_search = tk.Button(header, text="Find All", command=handle_search)
    btn_search.pack(side=tk.LEFT, padx=2)

    btn_clear = tk.Button(header, text="Clear", command=handle_clear)
    btn_clear.pack(side=tk.LEFT, padx=2)

    # Text Area (Body)
    text_area = tk.Text(root, wrap='word', height=15)
    text_area.pack(padx=10, pady=5, fill='both', expand=True)

    # Sample text for Text Area
    text_area.insert("1.0", """Python is a powerful language.\n
                     Tkinter makes GUIs easy.\n
                     Modular code is clean code!""")

    # Status Bar (Footer)    
    status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill='x')


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
    main_window = tk.Tk()
    user_interface(main_window)
    main_window.mainloop()
