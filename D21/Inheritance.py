# learning how to inherit attributes and methods from another class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # this is saying that fish extends animal
    def __init__(self):
        super().__init__()  # this is saying we want the attributes from the class we're inheriting from
        self.num_eyes = 4
        self.fins = 3

    def breathe(self):
        super().breathe()  # this is to add on to the inherited method's functionalities
        print("doing this underwater")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.breathe()
print(nemo.fins)