#!/usr/bin/env python3

# Logical Operators (and, or, not): used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

print(not(True)) # False
print(not(False)) # True
