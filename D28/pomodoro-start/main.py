from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_string = ""
timer = None  # this is to give it no value at all


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    checkmark.config(text="")  # resetting it to be empty
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    global checkmark_string
    checkmark_string = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global checkmark_string  # in order to keep track of how many pomodoro cycles
    global timer

    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)  # can also use an f string

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            checkmark_string += "✔"
            checkmark.config(text=checkmark_string)

        # alternatively, use a for loop
        # marks = ""
        # work_session = math.floor(reps/2)
        # for _ in range(work_session):
        #     marks += "✔"
        #     checkmark.config(text=checkmark_string)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=245, bg=YELLOW, highlightthickness=0)  # based on the size of the image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 124, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Label
title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# Start button
start_button = Button(text="Start", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmark label
checkmark = Label(bg=YELLOW, fg=GREEN, font=20)
checkmark.grid(row=3, column=1)

window.mainloop()
