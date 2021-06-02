#!/usr/bin/python3
""" 3. Same class or inherit from
    Write a function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function
    Args:
        obj: object to be listed
        a_class: data type to be compared
    Returns:
        object if is instance of...
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
