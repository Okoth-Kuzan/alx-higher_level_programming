#!/usr/bin/python3

import json
import csv
import os.path


class Base:
    """Base class for managing instances with common methods."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to save.
        """
        filename = f"{cls.__name__}.json"

        list_dic = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to convert.

        Returns:
            list: List of dictionaries.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class using a dictionary.

        Args:
            **dictionary: Dictionary containing attributes.

        Returns:
            object: Instance of the class.
        """
        new = cls(10, 10) if cls.__name__ == "Rectangle" else cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_cls = cls.from_json_string(f.read())

        return [cls.create(**item) for item in list_cls]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to save.
        """
        filename = f"{cls.__name__}.csv"

        list_keys = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']
        matrix = []

        for obj in list_objs:
            matrix.append([obj.to_dictionary()[key] for key in list_keys])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        list_keys = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']
        matrix = []

        for csv_elem in csv_list:
            dict_csv = {list_keys[kv[0]]: int(kv[1]) for kv in enumerate(csv_elem)}
            matrix.append(dict_csv)

        return [cls.create(**item) for item in matrix]

