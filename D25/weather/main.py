import pandas

data = pandas.read_csv("weather_data.csv")  # one data frame = one cell in an excel sheet
# a series is likened to a list in pandas

data_dict = data.to_dict()  # pandas allow the data type to be changed into several data types

temperature_list = data["temp"].to_list()  # converting the data into a list

# use the mean function from the pandas library instead
# average_temperature = sum(temperature_list) / len(temperature_list)
# print(average_temperature)

# print(f'The average temp for the week is: {data["temp"].mean()}')
# print(f'The max temp for the week is: {data["temp"].max()}')

# another way to use the column with pandas is
# print(data.condition)


# Get data in the rows of data frame
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])  # getting the row that corresponds to the maximum temperature

# go one step further, tapping into individual elements in the selected row
# example, converting the temp into farenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
farenheit = monday_temp * (9 / 5) + 32
# print(f'{farenheit} degree farenheit')

# creating a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Ben"],
    "scores": [76, 56, 65]
}
score_data = pandas.DataFrame(data_dict)
print(score_data)

# save as csv
score_data.to_csv("student_scores.csv")
