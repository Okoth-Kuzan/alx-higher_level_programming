#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    
    Parameters:
    a (int/float): First number to be added.
    b (int/float): Second number to be added. Defaults to 98
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    """Checking if both a and b are either integers or floats"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    """Casting a and b to integers if they are floats"""
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    """Return the addition of a and b as an integer"""
    return int(a + b)

