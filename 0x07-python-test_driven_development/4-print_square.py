#!/usr/bin/python3
""" 3. Print square
    Module Task 3
    Write a function that prints a square with the character #

"""


def print_square(size):
    """ print_square - function
        Args:
            size: size of a square to be printed
        Returns:
            nothing, only print a square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
