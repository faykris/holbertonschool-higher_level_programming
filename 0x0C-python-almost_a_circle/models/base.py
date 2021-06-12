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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method
        Returns:
             value of a list in JSON representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method
        Args:
            list_objs: objects lists to be stored into a JSON file
        """
        l_objs = []
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs is not None and len(list_objs) != 0:
                for key in list_objs:
                    l_objs.append(cls.to_dictionary(key))
            file.write(cls.to_json_string(l_objs))
            file.close()

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string static method
        Args:
            json_string: string inf JSON format
        Returns:
            json loaded to python
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create class method
        Args: dictionary for be processed
            dictionary:
        Returns:
            a new dictionary of objects
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load_from_file class method
        Returns:
            List of dictionaries of objects
        """
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ empty class"""
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ empty class"""
        pass
