print("Welcome to tip calculator.")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage would you like to tip? 10, 12, or 15? "))
num_diners = int(input("How many people to split the bill? "))

if (tip != 10 or tip != 12 or tip != 15):
    print("Invalid tip percentage")

percentage = float("1." + str(tip))

amount = (bill * percentage) / num_diners
final_amount = "{:.2f}".format(amount)
print(f"Each person should pay: ${final_amount}")
