#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int or float): The first number.
        b (int, optional): The second number. Defaults to 98.

    Return:
        int: The addition of a + b.

    Raises:
        TypeError: If a or b are not integers or floats.
        OverflowError: If a or b are too large to be converted to an integer.
        ValueError: If the string representation of a or b is too long.
        TypeError: If the wrong number of arguments are passed.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
