import random
import string

n_characters = int(input("How many characters would you like your password to have?\n > "))
n_numbers = int(input("How many numbers would you like your password to have?\n > "))
n_symbols = int(input("How many symbols would you like your password to have?\n > "))

password_list = []

for characters in range(n_characters):
    password_list.append(random.choice(string.ascii_letters))

for numbers in range(n_numbers):
    password_list.append(random.randint(0, 10))

for numbers in range(n_symbols):
    password_list.append(random.choice(string.punctuation))

random.shuffle(password_list)
password = ''.join(map(str, password_list))

print(f"Your new password is {password}")