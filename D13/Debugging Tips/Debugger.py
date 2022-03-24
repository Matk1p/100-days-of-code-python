#Use a Debugger

# the intention is to take a list, then return a list with elements with values double the original values of the elements in the list
# but the outcome is, it only prints 1 element in the list
# After breaking down the problem, the prime suspect is that the append() function is not called correctly, 
# To investigate this, can print the supposed appended item in every iteration
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    print(b_list)
  b_list.append(new_item)
  print(b_list)

# after being printed, we see that only the last elemt is appended
# this confirms the suspocion
# to fix this:

def mutate_v2(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate_v2([1,2,3,5,8,13])
