# # scenario 1, opening up a file that does not exist
# with open("a_file.txt") as file:
#     file.read()
#     # It will return an error
#     # FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

print("--------------------------------")

# # Scenario 2: Key Error, trying to look for a key that does not exist
# a_dict = {"Key": "value"}
# value = a_dict["non_existent_key"]
# print(value)
#
# # It will return an error
# # KeyError: 'non_existent_key

print("--------------------------------")

# # Scenario 3, Type Error, when trying to concatenate string and int, for example
# text = "abc"
# print(text + 3)
# # Returns TypeError: can only concatenate str (not "int") to str
