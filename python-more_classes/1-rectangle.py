#!/usr/bin/python3
'''
Module for a Rectangle
'''


class Rectangle:
    '''
    Class for a Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''
        Instantiation of a Rectangle

        Args:
            width (int): Width of a Rectangle (optional)
            height (int): Height of a Rectangle (optional)
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Private instance attribute that returns the width of a Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Private instance attribute that sets the width of a Rectangle

        Args: value (int): Value given to set the width of a Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Private instance attribute that returns the height of a Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Private instance attribute that sets the height of a Rectangle

        Args: value (int): Value given to set the height of a Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
