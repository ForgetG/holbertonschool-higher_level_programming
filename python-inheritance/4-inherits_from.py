#!/usr/bin/python3
'''Module 4-inherits_from'''


def inherits_from(obj, a_class):
    '''
    Public instance method that returns a boolean

    Args:
        obj (object): Given object
        a_class (type): the class to check against

    Return:
        bool:
            True if the object
            is an instance of a class that inherited (directly or indirectly)
            from the specified class;
        Otherwise:
            False
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
