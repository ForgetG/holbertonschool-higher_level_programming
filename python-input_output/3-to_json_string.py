#!/usr/bin/python3
'''Module 3-to_json_string'''
import json


def to_json_string(my_obj):
    '''
    Function that returns the JSON representation of an object

    Args: my_obj (string): object to return a JSON representation of

    Return: JSON representation
    '''
    return json.dumps(my_obj)
