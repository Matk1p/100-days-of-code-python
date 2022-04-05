from turtle import Turtle as t, Screen as s
from colours import rgb_colours
import random

tim = t()
screen = s()
tim.speed("fastest")
screen.colormode(255)
x_coordinate = -340
y_coordinate = -315

def draw_dot():
    x_coordinate = -340
    while x_coordinate <= 340:
        tim.pendown()
        tim.dot(15, random.choice(rgb_colours))
        tim.penup()
        tim.forward(34)
        x_coordinate += 34

while y_coordinate <= 315:
    tim.penup()
    tim.goto(x_coordinate, y_coordinate)
    draw_dot()
    y_coordinate += 35

screen.exitonclick()