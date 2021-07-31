#!/usr/bin/env python3

# Variable: a container for value. Behaves as the value that it contains 

# ================================================================================
# Strinrg
first_name = "Dliyaulhaq"
last_name = "Mufliansyah"
full_name = first_name + " " + last_name
print("Your name is: " + full_name)
# ================================================================================

# ================================================================================
# Int

Age = 15

# Cara 1:
# Age = Age + 1

# Cara 2:
Age += 1

print("Your age is: " + str(Age)) # Convert int to string
# ================================================================================

# ================================================================================
# Float

height = 167.5
print("Your height is: " + str(height) + "cm")
# ================================================================================

# ================================================================================
# Boolean

human = True
print("Are you a human?: " + str(human))
# ================================================================================

print("\nfull_name:", str(type(full_name)))
print("Age:", str(type(Age)))
print("height:", str(type(height)))
print("human:", str(type(human)))
