#!/usr/bin/python3
"""----- 5. Save Object to a file -----
    Write a function that writes an Object to a text file,
    using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """----- save_to_json_file function -----
     writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to be represented.
        filename: file for store the representation
    Returns:
        Nothing
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
        file.close()
