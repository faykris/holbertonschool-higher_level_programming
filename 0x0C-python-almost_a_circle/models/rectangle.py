#!/usr/bin/python3
"""
2. First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """
    @property
    def width(self):
        """ width getter method
            Return:
                self.__width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter method
            Args:
                width: width size os a object
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter method
            Return:
                self.__height
        """
        return self.__width

    @height.setter
    def height(self, height):
        """ height setter method
            Args:
                 height: height size os a object
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter method
            Return:
                self.__x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter method
            Args:
                 x: displacing in x
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter method
            Return:
                self.__y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ x setter method
            Args:
                 y: displacing in y
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init - constructor method
            Args:
                id: identification object
                width: width size of a object
                height: height size of a object
                x: displacing in x
                y: displacing in y
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ area method
            Returns:
                a value of are of a object
        """
        return self.__width * self.__height

    def display(self):
        """ display method
            Returns:
                a value of are of a object
        """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str method
            Returns: a string class value
        """
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update method
        Args:
            args: When receives simple args
            kwargs: When receives key value args
        """
        if args and args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
        elif kwargs and kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ to_dictionary method
        """
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
