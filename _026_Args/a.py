#!/usr/bin/env python3


# *args: Parameter that will pack all arguments into a tuple. Useful so that a function can accept a varying amount of arguments

def add(*numbers):
    sum = 0
    numbers = list(numbers)
    for i in numbers:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5))

