from turtle import Turtle

class Border(Turtle):
    """docstring for Border."""
    def __init__(self):
        super(Border, self).__init__(visible=False)
        self.penup()
        self.goto(-300,-300)
        self.pendown()

        for _ in range(4):
            self.fd(600)
            self.left(90)


