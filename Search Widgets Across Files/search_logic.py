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


def clear_tags(widget):
    """
    Removes all search-related highlighting tags from the text widget
    in order to prepare for a new search.

    Args:
        Pass the widget, pass the tag as parameters:
        widget: Whichevever tk.Text widget is targeted to be cleared.

    Raises:
        AttributeError: If the provided widget does not have a tag_remove method.
    """

    # Type checking: Ensure the widget actually has the required method
    if not hasattr(widget, "tag_remove"):
        raise AttributeError(f"The provided widget '{type(widget).__name__}' is not a valid Tkinter Text widget.")
    
    # widget.tag_names() returns a list of every tag currently in the widget
    for tag in widget.tag_names():
        # We usually skip the 'sel' tag as that's the user's mouse selection
        if tag != "sel":
            widget.tag_remove(tag, "1.0", tk.END)


def find_all(widget, query, startindex="1.0", stopindex="end", tag_name="found", **flags):
    """
    Locate all occurrence of 'query' and highlights each of them.
    Returns the total count of matches found.

    Args:
        widget: The tk.Text instance to be searched.
        query (str): The text string to find inside widget.
        startindex (str): The coordinate to begin searching. (Default "1.0") 
        stopindex (str): The coordinate to stop searching. (Default "end") 
        tag_name (str): The tag being applied to query results for highlighting. (Default "found")
        **flags: Expandable Tkinter search options to unpack (e.g., nocase=True, regexp=True).

    Returns:
        int: The number of matches found. (Displayed in Status Bar)
    """

    # Reset previous search state
    clear_tags(widget, tag_name)

    # Ensure that the query is not empty to avoid unnecessary processing
    if not query:
        # Todo: Add error message to status bar
        return None

    # Variable for counting instances of query
    count = 0
    current_pos = startindex  # Start from the top of the text widget by default

    # Default values for search flags to be unpacked in function call:
    search_flags = {
        'nocase' : True,    # Is search query case sensitive (e.g., 'smith' matches 'Smith')
        'regexp' : False     # Are there regular expression in search query?
        # Todo: Add more flags for an increasingly customizable search
    }

    """
    Note: Include a toggle for case sensitivity. 
    In Tkinter's .search() method, this is handled by a boolean flag:
    nocase=True (Ignore capitalization)
    nocase=False (Strict matching)
    """

    #  Merge the user-provided 'flags' into our settings
    search_flags.update(flags) # Overwrites defaults ONLY if the user provides an alternative

    # Search Loop:

    # Search and continue performing the search until stopindex
    while True:
        # Perform the search for the next occurrence
        # stopindex="end" prevents the search from wrapping around
        pos = widget.search(query, current_pos, stopindex=stopindex, **search_flags)

        # If no more matches are found, exit the loop
        if not pos:
            break

        # Mark the match
        end_pos = f"{pos}+{len(query)}c"     # Calculate end: 'pos' + 'length' characters ('c')
        widget.tag_add(tag_name, pos, end_pos)    # Apply tag to the string
    
        # Move the cursor forward to just after this match to find the next occurence of query
        current_pos = end_pos     # Place cursor at the end of the last occurence of query
        count += 1    # Keep a running count of how many instances of the query have been found

    # Visual configuration for the tag (IF there's only one type of tag)
    # widget.tag_config(tag_name, background="yellow", foreground="black")
    # Deprecated in favor of configuration dictionary in main.py

    return count


def find_next(widget, query, start_from="insert", tag_name="next", **flags):
    """
    Finds the next occurrence of the query starting from a specific index.
    Default 'start_from' is 'insert' (the current cursor position).
    """
    query = search_entry.get()
	
    if not query:
        update_status("Error: Enter text to find next.", "red")
        return None
	
	target_tag = "next" # This will use the "next" style from HIGHLIGHTING_CONFIGURATIONS

    # Setup search settings
    search_settings = {
		'nocase': True,  # Is search query case sensitive?
        'regexp': False  # Are there regular expression in search query?
		'backwards': False  # Keep search moving top to bottom
    }
    search_settings.update(flags)

    # Perform a single search from the current cursor position to the end
    pos = widget.search(query, start_from, stopindex=tk.END, **search_settings)

    if pos:
        # Clear only the 'next' highlight (Keep 'found' highlights visible)
        widget.tag_remove(tag_name, "1.0", tk.END)  # tag_name is specified in parameters
        
        # Calculate end value and apply the "next" tag
        end_pos = f"{pos}+{len(query)}c"

        # Calculate the span of the word
        widget.tag_add(tag_name, pos, end_pos)

        # Scroll to the next search result and move cursor there
        widget.mark_set("insert", end_pos) # This "saves" the position for the next click
        widget.see(pos)

        return pos

    return None


def get_match_count(widget, query, startindex="1.0", stopindex="end", **flags):
    """
    Returns the integer count of how many times the query appears in the widget.
    
    This "dry run" of the search logic does not apply any tags to the widget.

    Args:
        widget: The tk.Text instance to search.
        query (str): The text string to find.
        startindex (str): Where to begin the count.
        stopindex (str): Where to end the count.
        **flags: Search options (e.g., nocase=True, regexp=True).

    Returns:
        int: The total number of occurrences found.
    """

    # Check if there's a query
    if not query:
        return 0

    # Initialize the counter and starting position
    count = 0
    current_pos = startindex
        
    # Set default flags (matching your find_all logic)
    search_settings = {'nocase': True}
    search_settings.update(flags)

    while True:
        # Search for the next occurrence of query
        pos = widget.search(query, current_pos, stopindex=stopindex, **search_settings)
            
        if not pos:
            break
                
        # Increment count and move the pointer past this match
        count += 1
        current_pos = f"{pos}+{len(query)}c"
            
    return count

