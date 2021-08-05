#!/usr/bin/env python3

# Exeption: Events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    res = numerator / denominator
except ZeroDivisionError as e:
    print("========================================")
    print("Error: " + str(e))
    print("========================================")
except ValueError as e:
    print("========================================")
    print("Error: " + str(e))
    print("Enter only number plz")
    print("========================================")
except Exception:
    print("Something went wrong :(")
else:
    print(res) # Print when no exception
finally:
    print("Program end") # Whether or not we catch exception, this block of code always executed
