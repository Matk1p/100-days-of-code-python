# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# The issue is the conditional statement should not be or
# this will cause the code to enter the condition statement if the number is divisible by 3 or 5.
# The intended outcome is so that numbers that are both divisible by 5 AND 3 should be the ones that enter this if block.
# The next issue is that if statements should be followed by elif. If not, it will be considered as a whole new block and not a 2nd case
# the fix is as such:

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])