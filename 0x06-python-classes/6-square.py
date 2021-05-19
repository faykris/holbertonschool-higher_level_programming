#!/usr/bin/python3
"""6. Coordinates of a square
    Write a class Square that defines a square by: (based on 5-square.py)
    Private instance attribute: size:
    -   property def size(self): to retrieve it
    -   property setter def size(self, value): to set it:
        -   size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
        -   if size is less than 0, raise a ValueError exception with the
            message size must be >= 0
    Private instance attribute: position:
    -   property def position(self): to retrieve it
    -   property setter def position(self, value): to set it:
        -   position must be a tuple of 2 positive integers, otherwise
            raise a TypeError exception with the message position must be
            a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__
    (self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square
    area
    Public instance method: def my_print(self): that prints in stdout the
    square with the character #:
    -   if size is equal to 0, print an empty line
    -   position should be use by using space - Don’t fill lines by spaces
        when position[1] > 0
    You are not allowed to import any module
"""


class Square:
    """Square
        Init function to instance square size
        validate if a integer and if less than 0

    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method
            Args:
                size: size of square, must be integer >= 0
            Attributes:
                size: validate if a correct integer value
        """
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """Position - getter method
                    Returns:
                         the position tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position - setter method
                    validates the data if a valid tuple
        """
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """my_print
                print the square
        """
        for i in range(self.__size):
            print(" " * self.position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size <= 0:
            print()
