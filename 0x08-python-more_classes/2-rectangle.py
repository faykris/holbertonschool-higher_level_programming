#!/usr/bin/python3
"""2. Area and perimeter
    classes of module:
        Rectangle: print a rectangle
"""


class Rectangle:
    """Class Rectangle
        objects of this class who print a rectangle
    """
    def __init__(self, width=0, height=0):
        """Init Instance Method
            Args:
                width: horizontal size of a rectangle
                height: vertical size of a rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width - getter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width - setter

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height - getter

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height - setter

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ area - method
            Returns the area of rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """ perimeter method
            Returns the area of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)
