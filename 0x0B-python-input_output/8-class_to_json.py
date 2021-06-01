#!/usr/bin/python3
"""----- 8. Class to JSON -----
    Write a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """----- class_to_json function -----
    function that returns the dictionary description
    Args:
        obj: file for store the representation
    Returns:
        Object created.
    """
    return dict((key, value)for (key, value) in obj.__dict__.items())
