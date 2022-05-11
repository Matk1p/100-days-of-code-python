import datetime as dt
from random import randint
import pandas
import smtplib

MY_EMAIL = "webtester329@yahoo.com"
MY_PASSWORD = "gqlgozatktnqsduy"

now = dt.datetime.now()  # Takes in the current time
day_of_week = now.weekday()

df = pandas.read_csv("quotes.txt")
df_list = df.values.tolist()
chosen_quote = "'%s'" % "','".join(df_list[randint(0, 100)])
print(chosen_quote)

if day_of_week == 1:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()  # tls: transport layer security - encrypts the message, make it more secure
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="webtestercs102@gmail.com",
            msg="Subject:QOTD\n\n" + chosen_quote)  # can also use f string
