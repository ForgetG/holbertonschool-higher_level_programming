#!/usr/bibn/python3
'''Module 3-is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''
    Public instance method returning a boolean

    Args:
        obj (object): Given object to check
        a_class (type): The class to check against

    Return:
        bool: True if the object is
            an instance of the class that inherited from the specified class;
        Otherwise False
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
