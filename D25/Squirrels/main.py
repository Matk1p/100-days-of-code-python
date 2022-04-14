import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# counting how many squirrels of each colour there are
squirrel_colours = data["Primary Fur Color"].value_counts()
print(type(squirrel_colours))

# squirrel_dict = squirrel_colours.to_dict()
# print(squirrel_dict)
#
#
# key_list = list(squirrel_dict.keys())
# val_list = list(squirrel_dict.values())
# new_squirrel_dict = {
#     "Colour": key_list,
#     "Population": val_list
# }
# print(new_squirrel_dict)

# putting them into a new data frame
squirrel_colours.to_csv("Squirrel_colour_population.csv")
# this is inaccurate becuase the headings were off

# try using this
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")