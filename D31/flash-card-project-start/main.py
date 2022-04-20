from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 272, image=card_front_img)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# card_back_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 272, image=card_back_img)
# canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()