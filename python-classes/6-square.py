#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    Class for a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization that stores the size and position of a square

        Args:
            size (int): size of a square, default = 0
            position (tuple): position of the square,
            must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Public instance method that returns the area of the current square
        """
        return self.__size * self.__size

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
            value (int): Value given to set for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Private instance position attribute getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Private instance position attribute setter

        Args:
            value (tuple): Value given to set for position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Public instance method that prints the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
