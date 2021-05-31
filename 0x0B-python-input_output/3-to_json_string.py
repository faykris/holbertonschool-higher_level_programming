#!/usr/bin/python3
"""----- 3. To JSON string -----
    Write a function that returns the JSON representation of an
    object (string).
"""
import json


def to_json_string(my_obj):
    """----- read_file function -----
    function that returns the JSON representation of an object (string).
    Args:
        my_obj: name of file to be read.
    Returns:
         JSON representation
    """
    return json.dumps(my_obj)
