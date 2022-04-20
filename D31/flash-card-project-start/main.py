from tkinter import *
from random import choice
import time
import pandas

chosen_pair = {}

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- READ CSV ------------------------------- #
data_frame = pandas.read_csv("data/french_words.csv")
df_dict = data_frame.to_dict(orient="records")


# ---------------------------- FRENCH WORD ------------------------------- #
def next_card():
    global chosen_pair, flip_timer
    window.after_cancel(flip_timer)  # this will reset the timer everytime we change the card

    chosen_pair = choice(df_dict)
    chosen_word_french = chosen_pair['French']

    canvas.itemconfig(card, image=card_front_img)
    title = data_frame.columns[0]
    canvas.itemconfig(card_title, text=title, font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(card_word, text=chosen_word_french, font=("Ariel", 60, "bold"), fill="black")

    flip_timer = window.after(3000, func=card_back)


# ---------------------------- ENGLISH WORD ------------------------------- #
def card_back():
    canvas.itemconfig(card, image=card_back_img)

    chosen_word_english = chosen_pair["English"]
    back_title = data_frame.columns[1]
    canvas.itemconfig(card_title, text=back_title, font=("Ariel", 40, "italic"), fill="white")
    canvas.itemconfig(card_word, text=chosen_word_english, font=("Ariel", 60, "bold"), fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_back)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 272, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# card_back_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 272, image=card_back_img)
# canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
