weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# formatting the temp as 1 decimal place
weather_f = {day: "{:.1f}".format(temp * (9/5) + 32) for (day, temp) in weather_c.items()}


print(weather_f)


