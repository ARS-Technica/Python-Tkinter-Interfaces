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

# imports


def find_all(text_widget, query, tag_name="search"):
    # This is your primary engine.
    # Purpose: Loop through the entire document and apply a highlight tag to every match.
    # Logic: Uses a while loop with text_widget.search() and calculates the end_index for each match.

    pass


def clear_highlights(text_widget, tag_name="search"):
    # Resets the search tool so that it can be used again
    # Purpose: Remove the visual background/foreground colors from the widget.
    # Logic: Uses text_widget.tag_remove(tag_name, "1.0", "end").

    pass


def get_match_count(text_widget, query):
    # Display the number of matches found in the text.  Ex. "Found 5 matches."
    # Purpose: Return the integer count of how many times the string appears. 
    # Logic: A "dry run" of the search loop that increments a counter instead of applying tags.

    pass









