number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  
# the issue with this is the "=" sign, 
# in this case, "==" should be used to compare equality
# fixed code:

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")