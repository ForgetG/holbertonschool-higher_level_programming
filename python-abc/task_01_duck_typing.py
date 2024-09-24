#!/usr/bin/python3
'''Module task_01_duck_typing'''

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract class Shape inherits from ABC'''
    @abstractmethod
    def area(self):
        '''Abstract method area'''
        pass

    @abstractmethod
    def perimeter(self):
        '''Abstract method perimeter'''
        pass


class Circle(Shape):
    '''Subclass Circle inherits from Shape'''
    def __init__(self, radius):
        '''Instantiation of Circle'''
        self.__radius = radius

    def area(self):
        '''private instance method area of Circle'''
        return math.pi * self.__radius ** 2

    def perimeter(self):
        '''Private instance method perimeter of Circle'''
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    '''Subclass Rectangle inherits from Shape'''
    def __init__(self, width, height):
        '''Instantiation of Rectangle'''
        self.__width = width
        self.__height = height

    def area(self):
        '''Private instance method area of Rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Private instance method perimeter of Rectangle'''
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    '''Public instance method shape_info of shape'''
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
