#!/usr/bin/python3
'''Module 5-save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function that writes an Object to a text file
    using a JSON representation

    Args:
        my_obj (): Given Object
        filename (file): Given file
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
