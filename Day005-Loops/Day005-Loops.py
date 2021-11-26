# Example 1

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

# # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

val1=0
val2=0

for student_height in student_heights:
  val1 += 1
  val2 = val2 + student_height

avg_h=round((val2/val1),0)
print(avg_h)

# Another Approach

total_h = sum(student_height)
n_h = len(student_height)

#

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

val1=0
val2=0

for score in student_scores:
  if val1>val2:
    val2=val1

print (f"Valor Maximo eh : {val2}")



#Write your code below this row 👇
total=0
for n in range(0,101,2):
  total=total+n
print(total)

# Fizz Buzz

#Write your code below this row 👇

for n in range(1, 101):
  if n % 15 == 0:
    print("FizzBuzz")
  elif n % 5 == 0:
    print("Buzz")
  elif n % 3 == 0:
    print("Fizz")
  else:
    print(n)



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters=(random.sample(letters, nr_letters))
random_numbers=(random.sample(numbers, nr_numbers))
random_symbols=(random.sample(symbols, nr_symbols))

passw = ""

for n in random_letters:
  passw = passw + n
for n in random_numbers:
  passw = passw + n
for n in random_symbols:
  passw = passw + n

print(passw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

unified_list = random_letters + random_numbers + random_symbols
random.shuffle(unified_list)

passw = ""

for n in unified_list:
  passw = passw + n

print(passw)