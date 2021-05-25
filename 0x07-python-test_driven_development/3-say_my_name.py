#!/usr/bin/python3
""" 2. Say my name
    Module Task 2
    Write a function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """ say_my_name - function
        Args:
            first_name: name to be printed
            last_name: name to be printed ("" by default)
        Returns:
            nothing, only print a text
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
