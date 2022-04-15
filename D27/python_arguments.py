# this function can accept any number of arguments
# *args is the python convention to represent dynamic number of arguments
def print_numbers(*args):
    for n in args:
        print(n)


# takes in any number of arguments and returns its sum
def add(*args):
    return sum(args)


# kwargs = key word arguments, kwargs is basically a dictionary
def calculate(n, **kwargs):
    # print(kwargs["add"])  # this will return the value immediately without looping through the dict first
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:

    # this will allow our class to take in optional arguments, provide default values for the arguments not specified
    def __init__(self, **kw):
        # self.make = kw["make"]  # initialise like this is acceptable
        # self.model = kw["model"]
        # might be better to use the get. method so that if no input / args is being passed, it doesn't crash
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GTR")
# print(my_car.model)
