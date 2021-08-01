#!/usr/bin/env python3

# Loop Control Statement: Change a loops execution from its normal sequence

# break		: used to terminate the loop entirely
# continue	: skips to the next iteration of the loop
# pass		: does does nothing, acts as placeholder


# while True:
#     name = input("Enter your name: ")
#     print("Hello " + name)
#     if name != "":
#         break


# phone_number = "62-123-456-7890"
# for pn in phone_number:
#     if pn == "-":
#         continue
#     print(pn, end="")
# print()


for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)

