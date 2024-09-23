#!/usr/bin/python3
'''
Module that returns the
of available attributes and methods
of an object
'''


def lookup(obj):
    '''
    Function that returns
    the list of available attributes
    and methods of an object

    Args: obj (object): Given object

    Return: the list
    '''
    return dir(obj)
