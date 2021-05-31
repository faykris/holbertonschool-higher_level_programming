#!/usr/bin/python3
"""----- 1. Write to a file -----
    writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """----- write_file function -----
    writes a string to a text file (UTF8)
    Args:
        filename: name of file to be read.
        text: text to be added in the file
    Returns:
        the number of characters written
    """
    with open(filename, 'w') as file:
        nb_char = file.write(text)
        file.close()
        return nb_char
