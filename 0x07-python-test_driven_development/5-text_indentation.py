#!/usr/bin/python3
""" 4. Text indentation
    Module Task 3
    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ text_indentation - function
        Args:
            text: array text to be indented
        Returns:
            nothing, only print a text lines
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    array = ""
    t_len = 0
    for letter in text:
        t_len += 1
        array += letter
        if letter == "." or letter == "?" or letter == ":":
            print(array.strip())
            print()
            array = ""
        elif t_len == len(text):
            print(array.strip(), end="")
            array = ""
