#!/usr/bin/python3
'''
Module that defines a Square class
'''


class Square:
    '''
    Class for a square
    '''
    def __init__(self, size=0):
        '''
        Initialisation that store the size of a square

        Args: size(int): size of a square, default = 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        '''
        Public instance that return the area of the current square
        '''
        return (self.__size * self.__size)

    @property
    def size(self):
        '''
        size attribute property getter
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        size attribute property setter

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
        for i in range(self.__size):
            print('#' * self.__size)
