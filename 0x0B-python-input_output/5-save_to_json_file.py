#!/usr/bin/python3
"""----- 5. Save Object to a file -----
    Write a function that writes an Object to a text file,
    using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """----- from_json_string function -----
    function that returns an object (Python data structure)
    Args:
        my_obj: object to be represented.
        filename: file for store the representation
    Returns:
        Nothing
    """
    with open(filename, 'r+') as file:
        file.write(json.dumps(my_obj))
        file.close()
