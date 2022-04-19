# have a try catch block
# so instead of failing horribly, there is a backup plan just in case

# try : something that might cause an exception
# except : do this if there was an exception
# else : do this if there were no exceptions
# finally : do this no matter what happens - always going to be executed

# FileNotFound
# try:
#     file = open("a_file.txt")
# except:
#     # this is to at least let us know where the error happens, but it's better to handle it straight away
#     print("there was an error")

try:
    file = open("a_file.txt")
    a_dict = {"key" : "value"}
    print(a_dict["key"])
except FileNotFoundError:  # should specify the exception if not too broad
    file = open("a_file.txt", "w")  # this way, if the file is not found, it will create a new one
    file.write("something")
except KeyError as error_message:
    print(f"Key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()  # this block will execute no matter what

# the code in the try block will try to execute the codes line by line
# so it will try to execute all, but once it reaches a line where it can cause an exception,
# we need to catch that in the exception clause defined. If the except KeyError block is absent:
# then the error simply won't be caught, and the program will just crash, this way, we can at least know
# where to look for the source of the error
