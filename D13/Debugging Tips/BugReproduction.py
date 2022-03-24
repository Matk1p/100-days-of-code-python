# Reproduce the Bug
from random import randint

# here we have a list of numbers, stickers of dice
# we want to essentially "roll the dice" and return a random number
# so we have a random int
# we reproduce the code such that every time we run, we get the error exclusively isntead of occasionaly get an error
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# so if change the code  as such:
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6
# print(dice_imgs[dice_num])
# we will consistently get an index out of bounds error, so to fix this

dice_num = randint(0, 5)
print(dice_imgs[dice_num])