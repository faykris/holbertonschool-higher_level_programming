#!/usr/bin/python3
""" 12. My integer
    Write a class MyInt that inherits from int:
"""


class MyInt(int):
    """ MyInt Class
    """
    def __eq__(self, other):
        return not int.__eq__(self, other)

    def __ne__(self, other):
        return not int.__ne__(self, other)
