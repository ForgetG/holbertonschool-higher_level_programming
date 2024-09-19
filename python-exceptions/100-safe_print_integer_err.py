#!/usr/bin/python3
'''Module to print an integer safely'''
import sys


def safe_print_integer_err(value):
    '''
    Public function method that prints an integer safely

    Args: value (any data type): Given value to print

    Return:
        True: if value has been correctly printed
        False: if Exception is raised
    '''
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
