#!/usr/bin/python3
""" Defines a locked class"""

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value

