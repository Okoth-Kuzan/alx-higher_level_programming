#!/usr/bin/python3
"""
defines a class rectangle
"""
class Rectangle:
    """Class defining a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height"""
        self.__width = self.__validate_non_negative_int(width, "width")
        self.__height = self.__validate_non_negative_int(height, "height")

    def __validate_non_negative_int(self, value, attribute):
        """Validates and returns a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")
        return value

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.__width = self.__validate_non_negative_int(value, "width")

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.__height = self.__validate_non_negative_int(value, "height")

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

