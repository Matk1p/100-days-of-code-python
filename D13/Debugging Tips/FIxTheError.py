# Fix the Errors
# in this block of code, there is an indentation error being highlighted
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# in this, the indentation is fixed,
# but the bug comes because age needs to be an integer
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")


# this fixes the datatype integer issue
# but there is still an error, need to be an f string if we want to include values from variables
# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")

# this is fixed
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")