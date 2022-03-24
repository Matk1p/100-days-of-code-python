import random
import art
import os
import GameData

list = GameData.data
chosen_data = []


def clearConsole(): # purpose is to clear the screen after every round
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def get_option(list):
    position = random.randint(0, len(list) - 1) # choosing which data in the list is going to be displayed as either A or B
    while not is_chosen(position):
        position = random.randint(0, len(list))

    chosen_data.append(position)
    return list[position]


def is_chosen(position):
    if len(chosen_data) == 0:
        return True
    
    for i in range(len(chosen_data)):
        if position == chosen_data[i]:
            return False
        else:
            return True

def check_followers(option_a, option_b):
    # print(f'A follower count: {option_a["follower_count"]}')
    # print(f'B follower count: {option_b["follower_count"]}')
    if option_a["follower_count"] > option_b["follower_count"]:
        return "a"
    else: 
        return "b"

def guess_correct(guess, answer):
    if guess == answer:
        return True
    else:
        return False

score = 0 # to keep track of user score
idx = 0 # to pass in option B as the next round's option A
game_running = True # stopping condition for while loop

def game(score, idx, game_running):
    print(art.logo)

    while game_running:
        if score == 0:
            option_a = get_option(list)
        else:
            option_a = list[chosen_data[idx]]
            
        print(f"Your current score: {score}")
        print(f'Compare A {option_a["name"]}, a {option_a["description"]} from {option_a["country"]}')
        print(art.vs)
        option_b = get_option(list)
        print(f'Against B {option_b["name"]}, a {option_b["description"]} from {option_b["country"]}')

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess != "a" and guess != "b":
            print(f"Your guess, {guess} is invalid")
            game_running = False
            break
        elif not guess_correct(guess, check_followers(option_a, option_b)):
            print(f"You lost, your total score is {score}")
            game_running = False
            break
        else:
            score += 1
            idx += 1
            clearConsole()
            return game(score, idx, game_running)



game(score, idx, game_running)