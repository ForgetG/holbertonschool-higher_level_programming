#!/usr/bin/python3
'''Module 9-rectangle'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle class inherits from BaseGeometry class'''
    def __init__(self, width, height):
        '''Instantiation of the Rectangle'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Public instance method to calculate the area of the Rectangle
        '''
        return self.__height * self.__width

    def __str__(self):
        '''
        Public instance method to print a  specific string
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
