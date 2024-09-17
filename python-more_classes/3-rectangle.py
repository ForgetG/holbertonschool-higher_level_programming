#!/usr/bin/python3
'''Module for a Rectangle'''


class Rectangle:
    '''Class for a Rectangle'''
    def __init__(self, width=0, height=0):
        '''
        Instantiation of a Rectangle

        Args:
            width (int): Width of the Rectangle (optional)
            height (int): Height of the Rectangle (optional)
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Private instance attribute that returns the width of the Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Private instance attribute that sets the width of the Rectangle

        Args: value (int): Given value to sets the width of the Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Private instance attribute that returns the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Private instance attribute that sets the height of the Rectanlge

        Args: value (int): Given height to set the Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        '''
        Public instance method that returns the Rectangle area
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        Public instance method that returns the Rectangle perimeter
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        '''
        Public instance method that returns the Rectangle with #
        '''
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        else:
            for _ in range(self.height):
                rectangle += ("#" * self.width) + "\n"
        return rectangle[:-1]
