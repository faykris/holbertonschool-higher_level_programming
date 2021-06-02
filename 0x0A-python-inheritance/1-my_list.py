#!/usr/bin/python3
""" 1. My list
    Write a class MyList that inherits from list:
"""


class MyList(list):
    """MyList Class
    """

    def print_sorted(self):
        """print_sorted
            Public instance method
        """
        print(sorted(self))
