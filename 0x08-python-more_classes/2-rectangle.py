#!/usr/bin/python3

"""
This is a Rectangle class.
"""


class Rectangle:
    """ Rectangle this is an empty class"""

    def __init__(self, width=0, height=0):
        """
        initialize instance of Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter method for width
        """
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter method for width
        """
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        getter method for height
        """
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter method for height
        """
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """
    Calculate and returns area of Rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    Calculate and returns perimeter of Rectangle object.
    """
    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

