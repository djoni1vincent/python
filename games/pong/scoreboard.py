from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.color("white")

    def left_score(self):
        self.clear()
        self.goto(-50, 300)
        self.score_l += 1
        self.write(self.score_l)

    def right_score(self):
        self.clear()
        self.goto(50, 300)
        self.score_r += 1
        self.write(self.score_r)




