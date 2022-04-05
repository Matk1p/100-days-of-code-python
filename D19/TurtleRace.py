from turtle import Turtle as t, Screen as s
from random import randint

screen = s()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
x_coordinate = -230
y_coordinate = -100
all_turtles = []


# to set our turtles to their starting position
for i in range(len(color)):
    turtle_name = color[i]
    turtle_name = t(shape="turtle")
    turtle_name.color(color[i])
    turtle_name.penup()
    turtle_name.goto(x=x_coordinate, y=y_coordinate)
    y_coordinate += 30
    all_turtles.append(turtle_name)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # because the turtle itself is 40px wide
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle has won!")
            else:
                print(f"You've lost! The {winning_colour} turtle has won")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()