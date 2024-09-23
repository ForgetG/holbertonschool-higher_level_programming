#!/usr/bin/python3
'''Module 2-is_same_class'''


def is_same_class(obj, a_class):
    '''
    Public instance method that returns
    a boolean if the object is exactly an instance of the specified class

    Args:
        obj (object): Given object
        a_class (instance of class): instance of the specified class

    Return:
        True: if object is excaclty an instance of the specified class
        False: Otherwise
    '''
    return type(obj) is a_class
