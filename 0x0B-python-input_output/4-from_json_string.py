#!/usr/bin/python3
"""----- 4. From JSON string to Object -----
    Write a function that returns an object (Python data structure)
    represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """----- from_json_string function -----
    function that returns an object (Python data structure)
    Args:
        my_str: JSON to be represented.
    Returns:
        An object
    """
    return json.loads(my_str)
