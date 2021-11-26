def format_name(f_name, l_name):
  a = f_name.title()
  b = l_name.title()
  return f"{a} {b}"



print(format_name("diogo", "nomura"))

#############

## Days in Month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        v_is_leap = True
        # print("Leap year.")
      else:
        v_is_leap = False
        # print("Not leap year.")
    else:
      v_is_leap = True
      # print("Leap year.")
  else:
    v_is_leap = False
    # print("Not leap year.")
  return(v_is_leap)

def days_in_month(year, month):
  if (is_leap(year)) == False:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  else:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  days = month_days[month-1]
  return days
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)