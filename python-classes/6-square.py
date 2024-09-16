#!/usr/bin/python3
'''
Module that defines a Square class
'''


class Square:
    '''
    Class for a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialisation that store the size of a square

        Args:
                size(int): size of a square, default = 0
                position(int): position of the square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
            self.__position = position

    def area(self):
        '''
        Public instance that return the area of the current square
        '''
        return (self.__size * self.__size)

    @property
    def size(self):
        '''
        Private instance size attribute property getter
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Private instance size attribute property setter

        Args: value(int): Value given to set for size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif not isinstance(self.__size, int):
            raise TypeError("size must be >= 0")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def my_print(self):
        '''
        Public instance method that prints the square with the character #
        '''
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        '''
        Private instance position attribute getter
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Private instance position attribute setter
        '''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = int(value)
