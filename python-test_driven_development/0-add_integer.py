#!/usr/bin/python3
"""
Function add_integer takes 2 arguments, a and b.

Checks if the type of number is int or float.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int or float): The first number.
        b (int, optional): The second number. Defaults to 98.

    Return:
        The addition of a + b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
