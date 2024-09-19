#!/usr/bin/python3
'''Module that executes a function safely '''
import sys


def safe_function(fct, *args):
    '''
    Public function method that execute a function safely

    Args:
        fct (pointer): Pointer to a function
        *args : Argument(s) of the given function

    Return:
        result of the function
    Otherwise:
        None
    '''
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
