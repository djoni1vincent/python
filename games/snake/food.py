from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(randint(-250, 250), randint(-250, 250))
