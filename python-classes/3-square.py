#!/usr/bin/python3
'''
Module that defines a Square class
'''


class Square:
    '''
    Initialisation that stores the size of a square
    '''
    def __init__(self, size=0):
        '''
        Initialisation that store the size of square

        Args: size (int): size of square, default = 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        '''
        Public instance method that  returns the current square area
        '''
        return (self.__size * self.__size)
