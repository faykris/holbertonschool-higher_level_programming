#!/usr/bin/python3
""" 3. Same class or inherit from
    Write a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
"""


def inherits_from(obj, a_class):
    """inherits_from function
    Args:
        obj: object to be listed
        a_class: data type to be compared
    Returns:
        object if is instance of a class that inherited
        (directly or indirectly)
    """
    if not type(obj) == a_class and isinstance(obj, a_class):
        return True
    else:
        return False
