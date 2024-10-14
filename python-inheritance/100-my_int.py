#!/usr/bin/python3
"""Module 100-my_int"""


class MyInt(int):
    """MyInt class inherits from int"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
