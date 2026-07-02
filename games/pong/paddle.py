from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__(visible=True, shape="square")
        self.create_paddle()
        self.Y = 0
        self.goto(x,y)

    def create_paddle(self):
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(4, 1)

    def move_up(self):
        self.Y += 20
        self.sety(self.Y)

    def move_down(self):
        self.Y -= 20

        self.sety(self.Y)
