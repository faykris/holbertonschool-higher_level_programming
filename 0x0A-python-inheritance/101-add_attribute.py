#!/usr/bin/python3
""" Can I?
    Write a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(ob, na, va):
    """ add_attribute function
    Args:
        ob: object whose attribute has to be set
        na: attribute name
        va: value given to the attribute
    Returns:
        Nothing if successful, otherwise raise error
    """
    if '__dict__' in dir(ob):
        setattr(ob, na, va)
    else:
        raise TypeError("can't add new attribute")
