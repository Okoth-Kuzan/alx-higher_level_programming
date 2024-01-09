#!/usr/bin/python3

"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Store text content into a specified file using UTF-8 encoding.

    Args:
        filename (str): The name of the target file.
        text (str): The content to be written into the file.
        
    Returns:
        int: The count of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file_handle:
        return file_handle.write(text)

