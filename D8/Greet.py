
# function without parameters
def greet():
    print("Hello")
    print("How do you do?")
    print("How's the weather?")

# greet()

# function with one parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("How's the weather?")

# greet_with_name("MC Mikey")

# function with multiple parameters,
# postional argument: default way of calling the function
def greet_with(name, location):
    print(f"Hello {name}")
    print("How do you do?")
    print(f"How's the weather over in {location}?")

# greet_with("Mc Hammer", "Down under")
greet_with(location="Nowhere", name="Mc Hammer") #Keyword arguments, so the order of the arguments do not matter