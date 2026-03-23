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

















