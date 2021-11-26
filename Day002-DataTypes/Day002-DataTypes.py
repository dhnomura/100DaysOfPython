print("Hello"[0])

# Type Check

val1 = 123
print(type(val1))

# Type Conversion

val1 = len("Este eh um texto")
val2 = str(val1)

print ("teste " + val2)

print (70 + float("10.2"))

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# print (two_digit_number)

first_digit = int((two_digit_number[0]))

second_digit = int((two_digit_number[1]))

print(first_digit + second_digit)

# Mathematical Operations

print (3 + 5)
print (3 - 5)
print (3 * 5)
print (3 / 5)
print (3 ** 5)

# # PEMDAS # #
# Parentheses 
# Exponents
# Multiplication
# Division
# Addition
# Subtraction


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

# round

print(round(8/3))
print(round(2.6666666, 2))
print(8 // 3) # Floor Division

# Handle with variable operations

score = 10
score += 2
score -= 2
score *= 2
score /= 2


# f-String

print(f"your score is {score}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

total_years = 90
total_month = 90 * 12
total_weeks = 90 * 52
total_days  = 90 * 365

your_years  = age_as_int
your_month  = age_as_int * 12
your_weeks  = age_as_int * 52
your_days   = age_as_int * 365

days_left   = total_days - your_days
week_left   = total_weeks - your_weeks
month_left  = total_month - your_month

print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left.")

## Another Solution

years_remaining = 90 - age_as_int
month_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining  = years_remaining * 365

# Final Project, Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tips = input("What percentage tip would you like to give? 10, 12, 15? ")
peop = input("How many people to split the bill? ")

bill_as_int   = int(bill)
tips_as_float = float(tips)
peop_as_int   = int(peop)

adjust_tip    = (tips_as_float / 100 ) + 1
adjust_bill   = bill_as_int * adjust_tip
pay_per_pers  = round(adjust_bill / peop_as_int, 2)

print (f"Each person should pay: ${pay_per_pers}")
