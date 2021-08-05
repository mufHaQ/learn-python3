#!/usr/bin/env python3

import random, time

# Mode in open file: https://stackabuse.com/file-handling-in-python

try:
    with open('text.txt', 'w') as file:  # default is 'r'
        rng = 20
        for outer in range(1, rng+1):
            file.write("<=====> ")
            for inner in range(1, 15):
                lst = [file.write(str(random.randint(1, 100))), file.write(random.choice(
                    "!@#$%&*<>?")), file.write(random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))]
                file.write(str(random.choice(lst)))
            file.write("\n")
except Exception as e:
    print(e)
finally:
    with open('text.txt') as fl:
        print(fl.read())
