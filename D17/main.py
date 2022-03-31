class User:
    # pass  # the keyword that basically allows our classes / functions to remain empty for the time being
    # this is how to make a constructor in python
    # self just means the actual object being created / initialised
    def __init__(self, user_id, username):
        print("new user being created...")  # everytime a new instance of an object is created, this will run
        self.id = user_id
        self.username = username
        self.followers = 0  # this is to set the attribute with a default value
        self.following = 0

    def follow(self, user):  # every method needs to have a self parameter, this way, the method knows which obj called it
        user.followers += 1
        self.following += 1

user_1 = User("001", "John")
# to create an attribute inside the class
# user_1.id = "001"
# user_1.username = "Jack"

print(user_1)

# this is another way to initialise an instance of the object
user_2 = User("002", "Sam")
