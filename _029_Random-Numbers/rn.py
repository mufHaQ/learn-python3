#!/usr/bin/env python3

import random as r

# x = random.randint(1, 100) # Random number between 1 and 100
# y = random.random() # Random number between 0 and 1
# print(x)
# print(y)



myList = ["rock", "paper", "scissor"]
z = r.choice(myList) # Return random value from list
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
r.shuffle(cards) # Random all list values, No return value
print(cards)
