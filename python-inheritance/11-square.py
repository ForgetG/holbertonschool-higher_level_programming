#!/usr/bin/python3
'''Module 11-square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size):
        '''Instantioation of Square with size'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''
        Public instance method to calculate the area of the Square
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Public instance method to print a specific string
        '''
        return f"[Square] {self.__size}/{self.__size}"
