#!/usr/bin/python3
'''Module 1-write_file'''


def write_file(filename="", text=""):
    '''
    Function that writes a string to a textfile
    and returns the number of character written

    Args:
        filename (.txt): File to open or to create
        text (string): Text to write in the file

    Return: Number of character written
    '''
    with open(filename, encoding="utf-8", mode="a") as f:
        return f.write(text)
