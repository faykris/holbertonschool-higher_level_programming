#!/usr/bin/python3
"""----- 8. Class to JSON -----
    Write a class Student that defines a student by:
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

    @property
    def to_json(self):
        for (key, value) in self.__dict__.items():
            if value == self.first_name:
                return {key: value}
            if value == self.last_name:
                return {key: value}
            if value == self.age:
                return {key: value}
