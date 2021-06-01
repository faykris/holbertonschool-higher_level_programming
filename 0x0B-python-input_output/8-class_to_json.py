#!/usr/bin/python3
"""----- 6. Create object from a JSON file -----
    Write a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """----- class_to_json function -----
    creates an Object from a “JSON file”
    Args:
        obj: file for store the representation
    Returns:
        Object created.
    """
    return json.dumps(obj.__dict__)
