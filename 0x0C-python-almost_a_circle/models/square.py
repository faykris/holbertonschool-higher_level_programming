#!/usr/bin/python3
"""
2. First Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ init - constructor
        Args
            size: width and height of a object
            x: displacement in x
            y: displacement in y
            id: identification object
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """ str method
            Returns:
                The string value of a object
        """
        return "[Square] ({}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        """ width getter method
            Return:
                self.__width
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ width setter method
            Args:
                size: width size os a object
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def update(self, *args, **kwargs):
        """ update method
            Args:
                args: When receives simple args
                kwargs: When receives key value args
        """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ to_dictionary method
        """
        return {"id": self.id,
                "size": self.__size,
                "x": self.x,
                "y": self.y}
