#!/usr/bin/python3
"""----- 2. Append to a file -----
    Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """----- append_write function -----
    function that appends a string at the end of a text file (UTF8).
    Args:
        filename: name of file to be read.
        text: text to be appended
    Returns:
         the number of characters added.
    """
    with open(filename, 'a') as file:
        nb_char = file.write(text)
        file.close()
        return nb_char
