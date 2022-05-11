# Attempted to solve myself, but got stuck, could extract the date but the name was not tied to ensure the email is addressed to the correct recipient,
# using this opportunity to see how I could avoid the mistake

import datetime as dt
import pandas as pd
from random import randint
import smtplib

MY_EMAIL = "webtestercs102@gmail.com"
MY_PASSWORD = "comsci102"

today = dt.datetime.now()
today_tuple = (today.month, today.day)  # using this tuple to check against the DOB

data = pd.read_csv("birthdays.csv")

# get the information stored in a dictionary
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# check if today matches any of the dates in the dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        content = content.replace("Angela", "Rahmat")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
