#!/usr/bin/env python3

# Nested Loops: The "inner loop" will finish all of it's iterations before finishing one interation of the "outer loop"

rows = int(input("How many rows?: "))
column = int(input("How many columns?: "))
symbol = input("Enter a symbol: ")

for outer in range(rows):
    for inner in range(column):
        print(symbol, end="")
    print()
