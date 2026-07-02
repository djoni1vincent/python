from turtle import Turtle
SIZE = 273
# Border
class Border(Turtle):
    """docstring for Border."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pensize(3)
        self.color("white")


        self.penup()
        self.goto(-SIZE, -SIZE)
        self.pendown()

        for _ in range(4):
            self.forward(SIZE * 2)
            self.left(90)
