from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 250)
        self.write(f"level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER", font=FONT)

    def add_level(self):
        self.level += 1

