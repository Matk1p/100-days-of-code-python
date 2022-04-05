from turtle import Turtle as t, Screen as s

tim = t()

for _ in range(10):
    tim.pendown()
    tim.forward(10)
    tim.penup()  # pen not touching the "canvas" so it appears empty
    tim.forward(10)

screen = s()
screen.exitonclick()
