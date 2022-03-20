# Dictionary is a list that stores a key value pair

# to initialise a dictionary: dictionary = {key : value}
dictionary_example = {
    "Bug" : "An error in the program that prevents the program from runnning as expected.",
    "Function" : "A piece of code that you can easily call over & over again",
}

# Retrieving iterms from dictionary
# print(dictionary_example)

# Adding more items into the dictionary
dictionary_example["Loop"] = "The action of doing smth over and over again"
print(dictionary_example)

# how to initialise an empty dictionary
empty_dictionary = {}

# wipe an exiting dictionary
# dictionary_example = {}

# Edit an item in a dictionary
# find the key, then same as adding, but if it couldn't find the key, then it will add as a new entry
dictionary_example["Bug"] = "A moth in your computer"
print(dictionary_example)

# Looping through the dictionary
# this will just print the keys
for thing in dictionary_example:
    print(thing)

# to print the values
for key in dictionary_example:
    print(dictionary_example[key])