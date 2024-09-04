#!/usr/bin/python3
def pow(a, b):
    if a == 0 and b < 0:
        raise ValueError("0 can't be raised to a negative number")
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return result
