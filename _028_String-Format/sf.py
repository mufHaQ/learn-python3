#!/usr/bin/env python3

# str.format(): Optional method that gives users more control when displaying output


# ================================================================================
# animal = "cow"
# item = "moon"

# # print("The " + animal + " jumped over the " + item)

# # str.format()
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # Positional argument
# print("The {anml} jumped over the {itm}".format(anml="cow", itm="moon")) # Keyword argument
# ================================================================================

# ================================================================================
name = "Ulhaq"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # Add padding to the end

print("Hello, my name is {:<10}. Nice to meet you".format(name)) # Align left
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Align right
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Align center

print("{text}, my name is {name:^10}. Nice to meet you".format(text="Hello", name=name)) # Keyword argument with align
# ================================================================================

# ================================================================================
# f-string
print(f"\nHello, my name is {name}.")
# ================================================================================

# ================================================================================
# Number

number = 3.1411
bigNumber = 1000

print("\nThe number pi is {:.2f}".format(number)) # Get the 2 digits after decimal
print("The number is {:,}".format(bigNumber)) # Automatically add coma ','
print("The number is {:b}".format(bigNumber)) # Binary
print("The number is {:o}".format(bigNumber)) # Octal
print("The number is {:X}".format(bigNumber)) # HEXADECIMAL
print("The number is {:x}".format(bigNumber)) # hexadecimal
print("The number is {:E}".format(bigNumber)) # SCIENTIFIC NOTATION
print("The number is {:e}".format(bigNumber)) # scientific notation
# ================================================================================

