#!/usr/bin/python3
""" 8. Rectangle
    Write a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle
    """

    def __init__(self, width, height):
        """
        constructor of Rectangle class
        Args:
             width: value of width
             height: value of height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
