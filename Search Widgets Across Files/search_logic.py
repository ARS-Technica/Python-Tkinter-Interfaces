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


def clear_highlights(widget, tag_name="found"):
    """
    Removes all search-related highlighting from the text widget
    in order to prepare for a new search.

    Args:
        Pass the widget, pass the tag as parameters:
        widget: Whichevever tk.Text widget is targeted to be cleared.
        tag_name (str): The name of the tag to remove (Default is "found" for now).

    Raises:
        AttributeError: If the provided widget does not have a tag_remove method.
    """

    # Type checking: Ensure the widget actually has the required method
    if not hasattr(widget, "tag_remove"):
        raise AttributeError(f"The provided widget '{type(widget).__name__}' is not a valid Tkinter Text widget.")
    
    widget.tag_remove(tag_name, "1.0", "end")


def find_all(widget, query, tag_name="found", ignore_case=True):
    """
    Locate all occurrence of 'query' and highlights each of them.
    Returns the total count of matches found.

    Args:
        widget: The tk.Text instance to be searched.
        query (str): The text string to find.
        tag_name (str): The tag being applied to query results for highlighting.  

    Returns:
        int: The number of matches found.
    """
    
    # Reset previous search state
    clear_highlights(widget)

    # Ensure that the query is not empty to avoid unnecessary processing
    if not query:
        # Todo: Add error message to status bar
        return 0

    #Variable for counting instances of query
    count = 0
    start_pos = '1.0'   # Start from the top of the text widget

    
    # 2. Set the search flag for case sensitivity

    # 3. Perform the search        
    # If no more matches are found, exit the loop
 
    # 4. Mark the match
    # Calculate end: 'pos' + 'length' characters ('c')

    # 5. Move start_pos forward to just after this match

    # 6. Visual configuration for the 'found' tag

    pass


def find_next(text_widget, query, last_index):
    # "Find Next" functionality (like hitting F3 in a browser).
    # Purpose: Find only the match that appears after the current cursor position.
    # Logic: Takes a starting index as an argument and returns the position of next match.

    pass


def get_match_count(text_widget, query):
    # Display the number of matches found in the text.  Ex. "Found 5 matches."
    # Purpose: Return the integer count of how many times the string appears. 
    # Logic: A "dry run" of the search loop that increments a counter instead of applying tags.

    pass


