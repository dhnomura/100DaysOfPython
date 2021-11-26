#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Modules

import random

# GLOBAL Constant

L_NUMBERS=list(range(1, 101))

# Global Scope
pc_number=random.choice(L_NUMBERS)
print(pc_number)
n = 0

# Functions

def check_number():
  if pc_number == player_number:
    print(f"You find it: the number is {pc_number} ")
    return n + 10
  elif pc_number > player_number:
    print("Too low")
    return n + 1
  else:
    print("Too high")
    return n + 1

# Main
chances = input("Please choose hard or easy: ")
if chances == "hard":
  attempts = 5
else:
  attempts = 10

while n < attempts:
  player_number=int(input("Please guess a number : "))
  print(f"You have {attempts - n} attempts")
  n=(check_number())
