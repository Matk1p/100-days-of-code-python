file = open("/Users/Rahmat/Desktop/my_file.txt")
content = file.read()  # returns the content of the file as a string
print(content)  # can save the contents as a string variable

file.close()  # need to close so that python can free up the resource used up

# but many python developers do not use this way to open up files
# continued in the learningFiles_2.py
