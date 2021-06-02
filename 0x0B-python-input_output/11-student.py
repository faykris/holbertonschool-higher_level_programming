#!/usr/bin/python3
"""----- 11. Student to disk and reload -----
    Write a class Student that defines a student by: (based on 10-student.py)
    Public instance attributes:
    - first_name
    - last_name
    - age
"""


class Student:
    """----- Student function -----
        class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return dict(self.__dict__.items())
        for at in attrs:
            if type(at) != str:
                return dict(self.__dict__.items())
        r_dict = list()
        for key, value in self.__dict__.items():
            for attr in attrs:
                if attr == key:
                    r_dict.append([key, value])
        return dict(r_dict)

    def reload_from_json(self, json):
        for k in list(json.keys()):
            setattr(self, k, json[k])
