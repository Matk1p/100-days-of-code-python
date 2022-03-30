from decimal import Decimal


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = [0] # need to store and change the value of the money
def report():
    for item in resources:
        print(f"{item}: {resources[item]}")

    print(f"Money: ${money[0]}")

def check_resources(user_input):
    for key in resources:
        if resources[key] < MENU[user_input]["ingredients"][key]:
            print(f"Sorry there is not enough {resources[key]}")
            return False # need to fulfill both the ingredients and money condition to make the coffee
        else:
            return True

def coin_input():
    print("Please insert coins")
    quarter = Decimal(float(input("Quarters?: ")) * 0.25) # convert the amount of coins into its values
    dime = Decimal(float(input("Dimes?: ")) * 0.10)
    nickel = Decimal(float(input("Nickels?: ")) * 0.05)
    penny = Decimal(float(input("Pennies?: ")) * 0.01)

    return round((quarter + dime + nickel + penny), 2) # to make sure it stays true to the format of money

def check_sufficient_coins(coin_value, user_input):
    if coin_value < MENU[user_input]["cost"]:
        print(f'{coin_value} is less than cost of {user_input} -> {MENU[user_input]["cost"]}, You will be reimbursed')
        return False
    elif coin_value >= MENU[user_input]["cost"]: #making sure the amount input is bigger than the cost
        return True


def make_coffee(user_input, coin_value, money):
        money[0] += Decimal(MENU[user_input]["cost"])  # add to the value of money the machine currently holds
        change = coin_value - Decimal(MENU[user_input]["cost"])  # give back the change

        for key in resources:    
            resources[key] -= MENU[user_input]["ingredients"][key]  # update resources once coffee is made
        if change > 0:
            print(f"Here is your change: ${change}")
        
        print(f"enjoy your {user_input}!")


def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report()
    else:
        coin_value = coin_input()

        if check_resources(user_input) and check_sufficient_coins(coin_value, user_input):
            make_coffee(user_input, coin_value, money)

# to ensure the loop continues, based on user's choice
is_running = True
while is_running:
    coffee_machine()
    choice = input("Would you like to make aother transaction? 'Y' for yes, or 'N' for no ").lower()
    if choice == "n":
        is_running = False

print("Thank you for using the coffee Machine!")
