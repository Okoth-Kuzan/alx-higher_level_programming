#!/usr/bin/python3
""" a class to define a size of square """


class Square:
    """Square implementation"""

    def __init__(self, size=0):
        """Initialize the Square instance with a size (default is 0)"""
        self.__size = size

    def size(self):
        """Retrieve the size of the square"""

        return self.__size

    def size(self, value):
        """Set the size of the square with validation checks"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square"""

        return self.__size ** 2

