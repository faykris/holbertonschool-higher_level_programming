#!/usr/bin/python3
"""3. Area of a square
    Write a class Square that defines a square by: (based on 2-square.py)
    -   Private instance attribute: size
    -   Instantiation with optional size: def __init__(self, size=0):
        -   size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
        -   if size is less than 0, raise a ValueError exception with the
            message size must be >= 0
    -   Public instance method: def area(self): that returns the current
        square area
    -   You are not allowed to import any module
"""


class Square:
    """Square
        Init function to instance square size
        validate if a integer and if less than 0

    """
    def __init__(self, _Square__size=0):
        """__init__ method
            Args:
                _Square__size: size of square, must be integer >= 0
            Attributes:
                _Square__size: validate if a correct integer value
        """
        self._Square__size = _Square__size
        if type(_Square__size) != int:
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method
           Returns:
                The value of area of size of square -> A = S * S
        """
        return self._Square__size * self._Square__size
