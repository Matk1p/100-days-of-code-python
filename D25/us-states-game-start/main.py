import turtle

import pandas
import pandas as py

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# read the data from csv file
data = py.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # can get hold of the input with answer_state
    answer_state = screen.textinput(title=f"States correct: {len(guessed_states)}/50", prompt="What's another state name?").title()

    # if user wants to exit
    if answer_state == "Exit":
        # Generate a file that contains all the states the user couldn't guess for learning purposes
        # missed_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        #
        # applying list comprehension for cleaner code
        missed_states = [state for state in states_list not in guessed_states]

        df = pandas.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break
    # check if the user answers correctly
    if answer_state in states_list:  # can only use this method on lists
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
