#!/usr/bin/python3
for number1 in range(10):
    for number2 in range(number1 + 1, 10):
        if number1 < 8 or number2 < 9:
            print("{:02d}, ".format(number1 * 10 + number2), end="")
        else:
            print("{:02d}".format(number1 * 10 + number2))
