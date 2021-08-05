#!/usr/bin/env python3

# Nested Function Calls: Function calls inside other function calls. Innermost function calls are resolved first. Returned value is used as arguments for the next outer function


# 1
# num = input("Enter a whole positife number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# 2
print(round(abs(float(input("Enter a whole positife number: ")))))
