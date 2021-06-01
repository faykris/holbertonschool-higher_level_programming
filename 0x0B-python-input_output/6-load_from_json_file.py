#!/usr/bin/python3
"""----- 6. Create object from a JSON file -----
    Write a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """----- load_from_json_file function -----
    creates an Object from a “JSON file”
    Args:
        filename: file for store the representation
    Returns:
        Object created.
    """
    with open(filename, 'r') as file:
        j_file = file.read()
        file.close()
        return json.loads(j_file)
