#!/usr/bin/python3
""" 11. Square #2
    Write a class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class
    """

    def __init__(self, size):
        self._size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self._size, self._size)
