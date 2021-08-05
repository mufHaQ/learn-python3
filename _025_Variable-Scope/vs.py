#!/usr/bin/env python3

# Scope: The region that a variable is recognized. A variable is only available from inside the region it is created. A global and locally scoped version of a variable can be created

name = "Ulhaq" # Global scope (available inside & outside functions)

def display_name():
    name = "Dliya" # Local scope (available only inside this function)
    print(name)

display_name()

print(name)
