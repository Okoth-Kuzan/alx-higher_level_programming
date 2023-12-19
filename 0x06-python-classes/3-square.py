#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        Initialize the Square instance with a size (default is 0)
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
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

