################### Scope ####################

enemies = 1 # global scope example

def increase_enemies():
    enemies = 2 # Local scope example
# print(f"enemies inside function: {enemies}") #this will print the variable enemies as 2 always. 
# This is because, the variable "enemies" in the function belongs only in the function.
# Even though the variables are named the same, they are actually referring to different data
# Not a good practice to have the same names for local & global variables

increase_enemies()
# print(f"enemies outside function: {enemies}")

# 2 type of scopes, Global & Local, the only difference is where the variable is defined
# global variables are available / accessible by all fucntions 


# Namespace = anything that is given a name

# no such thing as block scope in python
enemies = ["zombies", "skeleton", "aliens"]
game_level = 3
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# notice how new_enemy can still be printed outside of the if block
# if statements do not count as a namespace block, variables can still be accessed outside the if blocks
# compare that to this

def get_enemy():
    enemies = ["zombies", "skeleton", "aliens"]
    game_level = 3
    if game_level < 5:
        test_new_enemy = enemies[0]

# print(test_new_enemy) # will return an error (variable not defined error) 

# this is just to prove how functions count as separate local scope but if blocks do not
# unlike in Java

