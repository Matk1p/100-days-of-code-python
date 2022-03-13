# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
str_name = name1.lower() + name2.lower()

true_score = str_name.count("t") + str_name.count("r") + str_name.count("u") + str_name.count("e") #find out the score by adding how 
#many letters in their names correspond to the phrase "true love"

love_score = str_name.count("l") + str_name.count("o") + str_name.count("v") + str_name.count("e")

score = str(true_score) + str(love_score)
score = int(score)

if (score < 10 or score > 90): print(f"Your score is {score}, you go together like coke and mentos")
elif(score >= 40 and score <= 50): print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")