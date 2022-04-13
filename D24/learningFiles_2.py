with open("/Users/Rahmat/Desktop/my_file.txt", mode="a") as file:  # this is so that we don't have to remember to file.close
    file.write("\nNew text.")

# mode="w" means writing, erasing everything in the file, then writing from scratch
# mode="a" is how to append to the file, does not erase the previously used contents

with open("/Users/Rahmat/Desktop/my_file.txt", mode="w") as new_file:  # if the file does not exist, this will create a new file for you, in mode="w"
    file.write("\nNew File")
