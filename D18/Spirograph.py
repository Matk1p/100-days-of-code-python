from turtle import Turtle as t, Screen as s
from random import randint

tim = t()
tim.speed("fastest")
screen = s()
screen.colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_circle(5)
screen.exitonclick()
