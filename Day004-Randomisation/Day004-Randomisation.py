# Heads or tails

import random

val1 = random.randint(0,1)

if val1 == 1:
  print("Heads")
else:
  print("Tails")


#############

# Random Name

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

val1=len(names)

print(names[random.randint(0,val1-1)])

# Another approach

print(random.choice(names))

#############

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

a=str(position)
col=int((a[0]))-1
lin=int((a[1]))-1

map[col][lin] = "x" 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


## Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["rock", "paper", "scissors"]
player1_opt = int(input("Make your choose : (1: Rock, 2: Paper, 3: Scissors) : "))-1
print(f"You choose {options[player1_opt]}")

if player1_opt == 0:
  print(rock)
elif player1_opt == 1:
  print(paper)
elif player1_opt == 2:
  print(scissors)

playerbot_opt = random.randint(0,2)
print(f"Bot choose {options[playerbot_opt]}")

if playerbot_opt == 0:
  print(rock)
elif playerbot_opt == 1:
  print(paper)
elif playerbot_opt == 2:
  print(scissors)

if player1_opt == playerbot_opt:
  print("Draw")
elif (
      (player1_opt == 0 and playerbot_opt == 2) or 
      (player1_opt == 1 and playerbot_opt == 0) or 
      (player1_opt == 2 and playerbot_opt == 1)  
    ):
    print("You Win!")
elif  (
      (player1_opt == 0 and playerbot_opt == 1) or 
      (player1_opt == 1 and playerbot_opt == 2) or 
      (player1_opt == 2 and playerbot_opt == 0)  
    ):
    print("You Lose!")



###### 

# Another Approach

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end