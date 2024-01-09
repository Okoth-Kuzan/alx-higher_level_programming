#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represents a student entity."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert Student object attributes to a JSON-like dictionary.

        Args:
            attrs (list): List of strings representing attributes.
                If provided, returns only those attributes.
        
        Returns:
            dict: Dictionary containing student attributes based on `attrs`.
                If `attrs` is None or invalid, returns all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

