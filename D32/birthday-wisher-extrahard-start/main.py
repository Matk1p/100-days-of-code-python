##################### Extra Hard Starting Project ######################
from random import randint, choice
import os
import pandas
import smtplib
import datetime as dt

MY_EMAIL = "webtestercs102@gmail.com"
MY_PASSWORD = "comsci102"

date_df = pandas.read_csv("birthdays.csv", usecols=['year', 'month', 'day'])

date_list = pandas.to_datetime(date_df)

now = dt.datetime.now()

random_letter = choice(os.listdir("letter_templates"))

for date in date_list:
    month = date.month
    day = date.day
    if (month == now.month) and (day == now.day):
        contents = random_letter.read()
        contents = contents.replace("NAME", "Rahmat")


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




