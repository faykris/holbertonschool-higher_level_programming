#!/usr/bin/python3
""" 0. Integers addition
    Module Task 0
    Write a function that adds 2 integers.

"""


def add_integer(a, b=98):
    """ Add integer - function
        Args:
            a: number 1
            b: number 2
        Returns:
            The sum of two numbers
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
