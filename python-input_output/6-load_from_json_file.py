#!/usr/bin/python3
'''Module 6-load_from_json_file'''
import json


def load_from_json_file(filename):
    '''
    Function that creates an Object from a JSON file

    Args: filename (.json): JSON file

    Return: Object created
    '''
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
