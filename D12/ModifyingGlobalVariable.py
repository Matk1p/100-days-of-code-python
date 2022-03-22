# modifying the global scope "enemies"
enemies = 1

def increase_enemies():
    global enemies # this is one way to access the gloabl scope BUT not a good practice - cofusing anc prone to creating bugs & error
    enemies += 1
    print(f"enemies inside fucntion: {enemies}")

# since its bad coding practice to simply call global variables, instead can use return, so this way we modified the variable w/o defining a new one
def increase_enemies_2():
    return enemies + 1

print(f"New number of enemies now: {increase_enemies_2()}")