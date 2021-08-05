#!/usr/bin/env python3

try:
    with open('text.txt') as fl:
        print("================================================================================")
        print(fl.read())
        print("================================================================================")
except FileNotFoundError as fnfe:
    print("Error: " + str(fnfe))
else:
    # print(fl.closed) # If it's True, file is closed

    if fl.closed:
        print("\nFile closed")
