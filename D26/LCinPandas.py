student_dict = {
    "student": ["Angie", "James", "Lily"],
    "score": [56, 70, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
# print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# looping through the data frame using pandas
# loops through each row of the data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angie":
        print(row.score)
