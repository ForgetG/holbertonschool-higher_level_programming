#!/usr/bin/python3
import sys
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

try:
    print_square(float("inf"))
except Exception as e:
    print(e)
print("")

try:
    print_square("5")
except Exception as e:
    print(e)
print("")

try:
    print_square('5')
except Exception as e:
    print(e)
print("")

try:
    print_square()
except Exception as e:
    print(e)
print("")

try:
    print_square(None)
except Exception as e:
    print(e)
print("")

try:
    print_square({"abc": 1, "def": 2})
except Exception as e:
    print(e)
print("")

try:
    print_square([1, 2, 3])
except Exception as e:
    print(e)
print("")

try:
    print_square(sys.maxsize + 1)
except Exception as e:
    print(e)
print("")