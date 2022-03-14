import random
import RPSprinter

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n > "))
computer_choice = random.randint(0, 2)

if user_choice <= 2 and user_choice >= 0:
    print("You chose " + str(RPSprinter.rps_printer(user_choice)))
    print("The computer chose " + str(RPSprinter.rps_printer(computer_choice)))

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("You lost!")
    else:
        print("You won!")
else:
    print("You've entered an invalid number, you lose by default")



    