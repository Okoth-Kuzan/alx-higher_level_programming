#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def size(self):
        """Getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    def size(self, value):
        """Setter of __size
        Args:
            value (int): the size of a side of the square
        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

