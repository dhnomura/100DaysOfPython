student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  # print(f"{grades} {student_scores[grades]}")
  if student_scores[student] > 90:
    student_grades[student]="Oustanding"
  elif student_scores[student] > 80:
    student_grades[student]="Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student]="Acceptable"
  else:
    student_grades[student]="Fail"
  

# 🚨 Don't change the code below 👇
print(student_grades)


############


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#DO NOT change the code above 👆

#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

#Do not change the code below 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)







# from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_dictionary = {}
stop_the_game = False

def person_bid(person, bid):
  bid_dictionary["Name"] = person
  bid_dictionary["Bid"] = bid

highest_bid = 0

# from art import logo

# print(logo)

should_end = False
while not should_end:

  person = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bid_dictionary[person] = bid

  restart = input("Type 'yes' to another bid. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    for n in bid_dictionary:
      bid_amount = int(bid_dictionary[n])
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = n
    print(f"The winner is {winner}, with {highest_bid}")
    print("Goodbye")
#   else:
    # clear()
    # print(logo)
    