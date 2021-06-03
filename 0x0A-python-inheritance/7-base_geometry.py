#!/usr/bin/python3
""" 7. Integer validator
    Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """ BaseGeometry Class
        with are method that shows an exception
    """

    def area(self):
        """ area method
            Returns:
                Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ area method
            Returns:
                Exception with message
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
