# Modules

import random
from art import logo
from art import vs
from game_data import data
from replit import clear

# Functions

def who_won():
  if score_a > score_b:
    return("A")
  elif score_a < score_b:
    return("B")
  else:
    return("Draw")

def random_list():
  global value_a
  global value_b
  global score_a
  global score_b
  if score==0:
    value_a=random.choice(data)
    value_b=random.choice(data)
    score_a=value_a['follower_count']
    score_b=value_b['follower_count']
  else:
    value_a=value_b
    value_b=random.choice(data)
    score_a=value_a['follower_count']
    score_b=value_b['follower_count']
  return(value_a)
  return(value_b)
  return(score_a)
  return(score_b)

# Variables

score=0
value_a='e'

# Main Program
random_list()
print(value_a)
should_end = False
while not should_end:
  clear()
  print(logo)
  if score>0:
    print(f"You're right! Current score: {score}.")

  print(f"Compare A: {value_a['name']}, a {value_a['description']}, from {value_a['country']}.")

  print(vs)

  print(f"Against B: {value_b['name']}, a {value_b['description']}, from {value_b['country']}.")
  answer=input(f"Who has more followers? Type 'A' or 'B': ").upper()
  winner=who_won()
  if answer == winner:
    print("Acerto misseravel")
    score+=1
    random_list()
  else:
    print("Errouuuu")
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    should_end = True





###################### S O L U T I O N ######################




from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.