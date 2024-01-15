#!/usr/bin/python3
""" Module that contains class Square, inheritance of class Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update the Square's attributes """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation of the Square """
        square_dict = super().to_dictionary()
        square_dict['size'] = square_dict.pop('width')
        return square_dict

