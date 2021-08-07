#!/usr/bin/env python3

# Rock, Paper, Scissors

import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

player = None

while player not in choices:
    player = input("Rock, Paper, Scissors?: ")

print("\nPlayes: " + player)
print("Computer: " + computer)

while True:
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        if computer == "Scissors":
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
        if computer == "Rock":
            print("You win!")
    else:
        if computer == "Rock":
            print("You lose!")
        if computer == "Paper":
            print("You win!")

    pa = input("\nPlay again? [y/n]: ")

    if pa == "n":
        break
