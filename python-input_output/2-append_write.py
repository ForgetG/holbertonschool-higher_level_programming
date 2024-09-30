#!/usr/bin/python3
'''Module 2-append_write'''


def append_write(filename="", text=""):
    '''
    Function that appends a string at the end of a text file
    and returns the number of characters added

    Args:
        filename (.txt): text file to open or to create
        text (string): text to be appendedat the end of the text file

    Return: Number of characters added
    '''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
