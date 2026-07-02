from turtle import Turtle

X = -225
Y = 460
# Border
class Border(Turtle):
    """docstring for Border."""
    def __init__(self):
        super().__init__(visible=False)
        self.speed(0)
        self.pensize(3)
        self.color("white")

        self.penup()
        self.goto(Y, X)
        self.pendown()

        for _ in range(2):
            self.left(90)
            self.fd(450)
            self.left(90)
            self.fd(925)
