#!/usr/bin/python3
"""5. Printing a square
    Write a class Square that defines a square by: (based on 4-square.py)
    -   Private instance attribute: size
        -   property def size(self): to retrieve it
        -   property setter def size(self, value): to set it:
            -   size must be an integer, otherwise raise a TypeError
                exception with the message size must be an integer
            -   if size is less than 0, raise a ValueError exception with
                the message size must be >= 0
    -   Instantiation with optional size: def __init__(self, size=0):
    -   Public instance method: def area(self): that returns the current
        square area
    -   Public instance method: def my_print(self): that prints in stdout
        the square with the character #:
        -   if size is equal to 0, print an empty line
    -   You are not allowed to import any module
"""


class Square:
    """Square
        Init function to instance square size
        validate if a integer and if less than 0

    """
    def __init__(self, size=0):
        """__init__ method
            Args:
                size: size of square, must be integer >= 0
            Attributes:
                size: validate if a correct integer value
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method
           Returns:
                The value of area of size of square -> A = S * S
        """
        return self.__size * self.__size

    @property
    def size(self):
        """size - getter method
            Returns:
                 the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size - setter method
            validates the data if a valid integer
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size <= 0:
            print()
