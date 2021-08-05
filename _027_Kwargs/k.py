#!/usr/bin/env python3

# **kwargs: Parameter that will pack all arguments into a dictionary. Useful so that a function can accept a varying amount of arguments

def hello(**names):
    # 1
    # print("Hello " + names["first_name"] + " " + names["last_name"])

    # 2
    print("Hello", end=" ")
    for val in names.values():
        print(val, end=" ")
    print()


hello(first_name="Dliyaulhaq", last_name="Mufliansyah")
