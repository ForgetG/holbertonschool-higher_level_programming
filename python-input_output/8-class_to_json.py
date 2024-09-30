#!/usr/bin/python3
'''Module 8-class_to_json'''


def class_to_json(obj):
    '''
    Function that returns the dictionnary description
    with simple data structure for JSON serialization of an object

    Args: obj (object): Given object

    Return: dictionnary description of object
    '''
    if isinstance(obj, object) and '__dict__' in dir(obj):
        return obj.__dict__
    return obj
