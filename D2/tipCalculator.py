print("Welcome to tip calculator.")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage would you like to tip? 10, 12, or 15? "))
num_diners = int(input("How many people to split the bill? "))

if (tip != 10 or tip != 12 or tip != 15):
    print("Invalid tip percentage")

percentage = float("1." + str(tip))

amount = round(((bill * percentage)) / num_diners, 2)
print(f"Each person should pay: ${amount}")
