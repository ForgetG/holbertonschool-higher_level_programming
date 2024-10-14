#!/usr/bin/python3
"""Module 101-add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
