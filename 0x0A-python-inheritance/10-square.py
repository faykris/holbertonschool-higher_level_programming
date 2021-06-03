#!/usr/bin/python3
""" 8. Rectangle
    Write a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class
    """

    def __init__(self, size):
        self._size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
