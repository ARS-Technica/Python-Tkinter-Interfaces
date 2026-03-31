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
    try:
        search_logic.clear_tags(text_area, tag_name="found")
        status_label.config(text="Highlights successfully cleared.", fg="black")
    except AttributeError:
        status_label.config(text="Error: Could not access text area.", fg="red")


def define_highlights(text_widget, styles_dict):
    """
    Iterate through a style dictionary and configures the widget tags.
    Maximizes modularity by eliminating the need to define highlights inside search.
    """
    for tag, colors in styles_dict.items():
        # **colors unpacks the dict into: background="yellow", foreground="black"
        text_widget.tag_config(tag, **colors)  

# apply_styles(text_area, HIGHLIGHTING_CONFIGURATIONS)


def on_search_click():
    # This is the "Bridge" or "Controller" function. It connects the UI to the search_logic.py
    # Purpose: Triggered when the user clicks "Search" or presses the Enter key.
    # Logic: Pulls the string from the Entry widget, calls find_all() from the logic file, and updates a status label.

    # apply_styles(text_area, HIGHLIGHTING_CONFIGURATIONS)


    pass


def on_clear_click():
    # The reset switch.
    # Purpose: Clears all highlights and empties the search box.
    # Logic: Calls clear_highlights() from the logic file and uses entry.delete(0, tk.END).

    pass


def update_status(message):
    # Reports the number of search instances in the document
    # Purpose: Updates a label at the bottom of the window (e.g., "Found 3 matches" or "No results").
    # Logic: Configures a tk.Label text property dynamically.

    pass


# USER INTERFACE  ------------------------------------------------------------------------

def user_interface(root):
    # Layout engine.  This function organizes the interface.
    # Purpose: Create the Text widget, the Entry field for searching, and the action buttons.
    # Logic: Uses Frames to group the "Search Tools" at the top and text input below.

    root = tk.Tk()
    root.title("Modular Tkinter Search")

    # Control Panel (Header)
    header = tk.Frame(root)
    header.pack(pady=10, padx=10, fill='x')

    # Search Form
    search_entry = tk.Entry(header)
    search_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=5)
    search_entry.bind("<Return>", lambda e: handle_search()) # Bind 'Enter' key

    btn_search = tk.Button(header, text="Find All", command=handle_search)
    btn_search.pack(side=tk.LEFT, padx=2)

    btn_clear = tk.Button(header, text="Clear", command=handle_clear)
    btn_clear.pack(side=tk.LEFT, padx=2)

    # Text Area (Body)
    text_area = tk.Text(root, wrap='word', height=15)
    text_area.pack(padx=10, pady=5, fill='both', expand=True)

    # Sample text for Text Area
    text_area.insert("1.0", "Python is a powerful language.\n
                     Tkinter makes GUIs easy.\n
                     Modular code is clean code!")

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


if __name__ == "__main__":
    root.user_interface()
    root.main()

