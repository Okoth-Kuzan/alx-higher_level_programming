#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text content to be written into the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

