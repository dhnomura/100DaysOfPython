# Odd or Even

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

check_num = number % 2
print (check_num)

if check_num > 0:
  print("Odd")
else:
  print("Event")

# Another Approach

#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")


#######################

# BMI Calculator

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = round(weight / (height ** 2))

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:  
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


## Leap Year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (year % 4) != 0:
  print("Not leap year.")
else:
  if (year % 100) != 0:
    print("Leap year.")
  else:
    if (year % 400) != 0:
      print("Not leap year.")
    else:
      print("Leap year.")


## Multiple IFs

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


# Pizza Bill

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Logical Operators

### Score Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

l_name1=name1.lower()
l_name2=name2.lower()

counter11 = 0
counter12 = 0
counter21 = 0
counter22 = 0

val11=int(l_name1.count("t"))
val12=int(l_name2.count("t"))
counter11 += val11
counter12 += val12
val11=int(l_name1.count("r"))
val12=int(l_name2.count("r"))
counter11 += val11
counter12 += val12
val11=int(l_name1.count("u"))
val12=int(l_name2.count("u"))
counter11 += val11
counter12 += val12
val11=int(l_name1.count("e"))
val12=int(l_name2.count("e"))
counter11 += val11
counter12 += val12

first_counter = counter11 + counter12

val21=int(l_name1.count("l"))
val22=int(l_name2.count("l"))
counter21 += val21
counter22 += val22
val21=int(l_name1.count("o"))
val22=int(l_name2.count("o"))
counter21 += val21
counter22 += val22
val21=int(l_name1.count("v"))
val22=int(l_name2.count("v"))
counter21 += val21
counter22 += val22
val21=int(l_name1.count("e"))
val22=int(l_name2.count("e"))
counter21 += val21
counter22 += val22
second_counter = counter21 + counter22

score = int(str(first_counter) + str(second_counter))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
if score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



# Another Approach

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


## Teasure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")



#####

## Capitais do Brasil

print('''
      .  .-+  ._/V\\
     / \/   \/    /__
    )                "-+._
   ."                     \\
  (       B R A S I L      )
   \                      /
     \__                 (
        >_               )
          \_.           /
             < S.Paulo /
              \   *  _/
               >    /
              /    /
             <    /
              "^./
''')
print("Bem vindo ao teste de geografica.")
print("Voce consegue identificar todas as capitais brasileiras? ")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")