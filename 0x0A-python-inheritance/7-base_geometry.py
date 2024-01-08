#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    def area(self):
        """Raises an Exception as area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

