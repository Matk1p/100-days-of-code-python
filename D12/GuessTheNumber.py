import random
import GTNArt

THE_NUMBER = random.randint(1, 100)
difficulty = ""
EASY_LIFE = 10 # not going to change these 2 values 
HARD_LIFE = 5

def game_start():
    print(GTNArt.logo)
    print("Welcome to GuessTheNumber!")
    print("I'm thinking of a number between 1 - 100")
    difficulty = input("Choose a difficulty. Type 'easy', or 'hard': ").lower()
    return difficulty

def life_generator(difficulty):
    if difficulty == "easy":
        print(f"You have {EASY_LIFE} attempts remaining to guess the number")
        return EASY_LIFE
    elif difficulty == "hard":
        print(f"You have {HARD_LIFE} attempts remaining to guess the number")
        return HARD_LIFE
    else:
        return "Invalid difficulty"

def number_checker(guessed_number, current_life):
    if guessed_number == THE_NUMBER:
        print(f"Congratulations! You guess the right number {THE_NUMBER}! You win!")
        return True
    elif guessed_number < THE_NUMBER:
        print(f"{guessed_number} is too low. You have {current_life - 1} lives left")
        return False
    elif guessed_number > THE_NUMBER:
        print(f"{guessed_number} is too high. You have {current_life - 1} lives left")
        return False

difficulty = game_start() #take into consideration user choice for difficulty
still_alive = True # stopping condition for while loop
current_life = life_generator(difficulty)
while still_alive or current_life > 1: # if goes to 0, then it gives 1 extra attempt
    guessed_number = int(input("Make a guess: "))
    if number_checker(guessed_number, current_life) == True or current_life == 1: #check if user ran out of lives or guess the word correctly
        still_alive = False
        break
    current_life -= 1

# give user the satisfaction of knowing what is the right answer
if current_life == 1:
    print(f"You ran our of lives. The number was {THE_NUMBER}")

