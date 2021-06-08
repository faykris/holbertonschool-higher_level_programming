#!/usr/bin/python3
"""
1. Base class
"""
import json
import os.path


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
            list_objs: objects lists to be stored into a JSON file
        """
        l_objs = []
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs is not None:
                for key in list_objs:
                    l_objs.append(cls.to_dictionary(key))
            file.write(json.dumps(l_objs))
            file.close()

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(12, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        l_dic = []
        if not os.path.exists("{}.json".format(cls.__name__)):
            return l_dic
        with open("{}.json".format(cls.__name__), "r") as file:
            j_file = file.read()
            r_file = cls.from_json_string(j_file)
            for dic in r_file:
                l_dic.append(cls.create(**dic))
            file.close()
            return l_dic
