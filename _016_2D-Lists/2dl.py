#!/usr/bin/env python3

# 2D Lists: a list of lists

drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

# print(food[2][1]) # ice cream


for index, wrapper in enumerate(food, start=1):
    if index == 1:
        print("drinks:")
    elif index == 2:
        print("dinner:")
    else:
        print("dessert:")
    
    for index, inner in enumerate(wrapper, start=1):
        print(str(index) + ". " + inner)
    print()
    # for inner in wrapper:
        
