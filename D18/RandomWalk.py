from turtle import Turtle as t, Screen as s
from random import randint

tim = t()
tim.pensize(5)
tim.speed("fastest")
screen = s()
screen.colormode(255)


def random_direction(number):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    if number == 0:
        tim.forward(20)
    elif number == 1:
        tim.left(90)
        tim.forward(20)
    else:
        tim.right(90)
        tim.forward(20)


for _ in range(100):
    random_direction(randint(0, 2))

# alternatively, can use the setHeading() function from turtle

screen.exitonclick()
