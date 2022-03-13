print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroads choose whther you want to go? Type "left" or "right"? > ').lower()
if (choice1 == "left"): 
    choice2 = input('Now you need to make a choice, either swim or wait. Type "swim" or "wait" > ').lower()
    if(choice2 == "wait"):
        print("You have waited and it paid off, you found a boat and took it to the island")
        choice3 = input('Now you need to choose the door to the treasure, choose "red", "blue" or "yellow"? Chooose wisely > ').lower()
        if(choice3 == "blue"):
            print("Congratulations! You have attained the one piece!")
        elif(choice3 == "red"):
            print("Your left hand got bitten by a sea monster. GAME OVER")
        else:
            print("You got turned into stone. GAME OVER")
    else:
        print("You forgot you couldnt swim and got bested by the sea. GAME OVER")
else:
    print("You fell into a hole. GAME OVER")