# CSV just means, comma separated values
# in this file, we learn the many different ways of reading data from a CSV file

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) # extracting data in this way will require a lot of formatting

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # this will return us a CSV object
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     # temperatures.pop(0)  # to remove the column heading, alternatively, can use if statement
#     print(temperatures)


import pandas  # using pandas library for better reading of CSV files

data = pandas.read_csv("weather_data.csv")
# print(data)  # printing the entire contents of the file
print(data["temp"])  # specifying which column to print
