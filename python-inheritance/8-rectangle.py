#!/usr/bin/python3
'''Module 8-rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle class inherits from BaseGeometry class'''
    def __init__(self, width, height):
        '''Instantiation of the Rectangle'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
