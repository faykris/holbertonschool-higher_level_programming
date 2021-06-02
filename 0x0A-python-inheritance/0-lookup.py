#!/usr/bin/python3
""" 0. Lookup
    Write a function that returns the list of available attributes
    and methods of an object:
"""


def lookup(obj):
    """lookup function
    Args:
        obj: object to be listed
    Returns:
        list of available attributes
    """
    return dir(obj)
