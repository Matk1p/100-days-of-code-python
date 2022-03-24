# Play Computer
# For this case, if the user inputs the year 1994, nothing will be printed
# This is because the computer will accept anything between 1981 - 1993 (inclusive) and 1995 (inclusive) onwards
# This will end up with 1994 not being handled
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

  # in order to avoid this, simply use <= if we want to include 1994 as millenial
  # or >= in elif if 1994 is a gen Z

# the fixed code looks like this: 
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")