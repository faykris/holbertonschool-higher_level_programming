#!/usr/bin/python3
""" 2. Exact same object
    Write a function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """is_same_class function
    Args:
        obj: object to be listed
        a_class: data type to be compared
    Returns:
        True if object is exactly an instance of the specific class
        otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
