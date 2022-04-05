from turtle import Turtle, Screen
# Screen is part of the turtle module

# can give the module aliases also
# from turtle import Tutle as t
timmy = Turtle()
timmy.shape("classic")
timmy.color("aquamarine1")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

# this is to ensure we can see the pop-up window
screen = Screen()
screen.exitonclick()
