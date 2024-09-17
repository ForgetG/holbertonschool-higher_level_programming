#!/usr/bin/python3
'''Module for a Rectangle'''


class Rectangle:
    '''Class for a Rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        Instantiation of the Rectangle

        Args:
            width (int): Width of the Rectangle (optional)
            height (int): Height of the Rectangle (optional)
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        Args: value (int): Given value to set the width of the Rectangle
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
        Private instance attribute that sets the height of the Rectangle

        Args: value (int): Given value to set the height of the Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''
        Public instance method that returns the Rectangle area
        '''
        return (self.__height * self.__width)

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
            symbol = str(self.print_symbol)
            for _ in range(self.__height):
                rectangle += (symbol * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        '''
        Public instance method that returns:
            a string representation of the Rectangle
        '''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''
        Public instance method finalizer:
            that prints a message when a instance of Rectangle is deleted
        '''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Static method that returns the biggest rectangle based on the area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''
        Class method that returns:
            A new Rectangle instance with width == height == size
        '''
        return cls(size, size)
