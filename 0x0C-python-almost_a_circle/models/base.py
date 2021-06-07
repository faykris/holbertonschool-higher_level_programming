#!/usr/bin/python3
"""
1. Base class
"""
import json


class Base:
    """Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor
        Args:
            id: identification code
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ to_json_string method
        Returns:
             value of a list in JSON representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method
        Args:
            list_objs:
        Returns:
             I don't know
        """
        if list_objs is None:
            return []
        with open("Rectangle.json", "w") as file:
            file.write(cls.to_json_string([1, 2, 3]))  # hardcoded value - must be replaced
            file.close()
        return
