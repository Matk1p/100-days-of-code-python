from random import randint

# accessing the lists / dictionary in a more effective manner

# traditionally, to add 1 to a list in a dictionary, a for loop
my_list = [1, 2, 3]
new_name_list = []
for num in my_list:
    add_1 = num + 1
    new_name_list.append(add_1)

# in list comprehension, we can do smth like this
numbers = [1, 2, 3]
# new_numbers = [new_item for item in list] replace, new_item with the operation we intend to carry out
# replace item with the item we're iterating through, replace list with the actual list we're iterating through
new_numbers = [num + 1 for num in numbers]

name = "Angela"
new_name_list = [letter for letter in name]

# conditional list comprehensions
# new_list = [new_item for item in list if test] guide syntax
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]  # only adds into the new list if it passes the < 5 len test
long_upper_case_name = [name.upper() for name in names if len(name) > 5]
# print(long_upper_case_name)

