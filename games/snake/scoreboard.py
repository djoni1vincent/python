
from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)

    def food_eaten(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center")

