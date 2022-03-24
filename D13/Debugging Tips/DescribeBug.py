# # Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# purpose of function is to get the line printed
# line is printed when the value of i is 20
# but the line is not printed

# Assumption -> i here will definitely have the value of 20 at some point
# assumption is wrong as range function is exclusive of the ceiling
# to solve, simply change from ceil 20 to ceil 21
# like so

def my_function_2():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function_2()