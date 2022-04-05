from turtle import Turtle as t, Screen as s
from random import randint

tim = t()
screen = s()
angle = 360  # starting angle
sides = 3  # starting number of sides in shape (triangle)
screen.colormode(255)


def draw_shape(sides, angle):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle / sides)


for sides in range(3, 11):
    draw_shape(sides, angle)

screen.exitonclick()
