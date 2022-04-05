from turtle import Turtle as t, Screen as s

tim = t()
screen = s()


def move_forward():
    tim.forward(10)


#  higher order function - taking a function as a parameter in another function
#  good practice to use keyword arguments in a function instead of positional arguments when it comes to functions
#  not created by myself
screen.listen()  # will start taking in user input as new commands
screen.onkey(key="space", fun=move_forward)  # remove the parentheses in the method being passed in
screen.exitonclick()
