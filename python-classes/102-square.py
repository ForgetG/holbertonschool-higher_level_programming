#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    Class for a square
    """
    def __init__(self, size=0):
        """
        Initialization that stores the size of a square

        Args:
            size (int or float): size of a square, default = 0
        """
        self.size = size

    @property
    def size(self):
        """
        Private instance size attribute property getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Private instance size attribute property setter

        Args:
            value (int or float): Value given to set for size
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method that returns the area of the current square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Equality comparator for squares based on area
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator for squares based on area
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparator for squares based on area
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparator for squares based on area
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparator for squares based on area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparator for squares based on area
        """
        return self.area() >= other.area()
