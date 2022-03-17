from dis import dis
import random
import HangManArt
import hangManWordList

print(HangManArt.logo)
word_list = hangManWordList.word_list
generated_word = random.choice(word_list) #the word they're going to guess
life = 5

def word_guessed_correctly(word):
    for i in range(len(word)):
        if word[i] == "_":
            return False
    
    return True

def is_repeated_guess(letter):
    for i in range(len(displayed_string)):
        if letter == displayed_string[i]:
            print(f"You've already guessed the letter: {letter}")
            return False
    
    return True

# wrong letters are in a separated function because they are stored in a different variable
def is_repeated_wrong_guess(letter):
    if len(guessed_wrong_list) == 0: return True

    for i in range(len(guessed_wrong_list)):
        if letter == guessed_wrong_list[i]:
            print(f"You've already guessed the letter: {letter}")
            return False
    
    return True


displayed_string = []
for i in range(len(generated_word)):
    displayed_string.append("_")

print(''.join([str(i) for i in displayed_string]))
print("\n")
print("++++++++++++++++++++++++++++++")
guessed_wrong_list = []

while life > 0:
    guessed_letter = input("Which letter would you like to guess?\n > ").lower() #make sure the word guessed is in lower cases

    if not is_repeated_guess(guessed_letter): continue # check for repeated guess
    if not is_repeated_wrong_guess(guessed_letter): continue 
        
    guessed_wrong = False
    for i in range(len(generated_word)):
        if guessed_letter == generated_word[i]:
            displayed_string[i] = guessed_letter
            guessed_wrong = True

    print(''.join([str(i) for i in displayed_string]))

    if guessed_wrong == False: 
        guessed_wrong_list.append(guessed_letter)
        print("Theses letters are not in the word: " + str(guessed_wrong_list))
        print(f"You have {life - 1} lives left")
        print(HangManArt.stages[life])
        life -= 1
    
    if word_guessed_correctly(displayed_string):
        print("Congratulations, you have successfully guessed the word!")
        break

if life == 0:    
    print(f"The word was {generated_word}")
    print("You ran out of lives, GAME OVER")
    print(HangManArt.stages[0])
