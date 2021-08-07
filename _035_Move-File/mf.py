#!/usr/bin/env python3

import os


source = "text.txt"
destination = "dir/" + source

try:
    if os.path.exists(destination):
        print("File already exists!")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as fne:
    print("Error: ", fne)

