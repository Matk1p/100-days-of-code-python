#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
    contents = contents.replace("Angela", "Rahmat")

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.read()  # can also use the name_file.readlines() function to immediately get them in the list forms
    name_list = names.split('\n')  # getting the names of invited guests in a string form

    for name in name_list:
        new_content = contents.replace("[name]", name)
        file_extension = name + ".txt"
        fileName = "Output/ReadyToSend/" + file_extension
        with open(fileName, mode="w") as output_file:
            new_content = contents.replace("[name]", name)
            output_file.write(new_content)


