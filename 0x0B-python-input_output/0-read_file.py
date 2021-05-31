#!/usr/bin/python3
"""----- 0. Read file -----
    Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """----- read_file function -----
    Read and print file using with statement
    Args:
        filename: name of file to be read.
    Returns:
        Nothing.
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
        file.close()
