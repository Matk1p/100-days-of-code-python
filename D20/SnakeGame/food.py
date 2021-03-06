from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):  # get the food to go to a new random location once eaten
        random_x_coordinate = randint(-280, 280)
        random_y_coordinate = randint(-280, 280)
        self.goto(x=random_x_coordinate, y=random_y_coordinate)