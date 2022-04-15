
with open("file1.txt") as file_1:
    list_1 = [int(line.strip()) for line in file_1.readlines()]

with open("file2.txt") as file_2:
    list_2 = [int(line.strip()) for line in file_2.readlines()]


# print(list_1)
# print(list_2)
result = [num for num in list_1 if num in list_2]
# Write your code above 👆

print(result)


