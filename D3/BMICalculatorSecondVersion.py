import math
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = (weight / (height * height))
BMI = math.ceil(BMI)

if (BMI > 35):
    print(f"Your BMI is {BMI}, you are critically obese")
elif (BMI <=35 and BMI > 30):
    print(f"Your BMI is {BMI}, you are obese")
elif (BMI <= 30 and BMI > 25):
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif(BMI <= 25 and BMI > 18.5):
    print(f"Your BMI is {BMI}, you have a normal weight")
elif (BMI < 18.5):
    print(f"Your BMI is {BMI}, you have a normal weight")

        