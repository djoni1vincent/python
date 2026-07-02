from turtle import Turtle, home
class Guessed(Turtle):
    def __init__(self, x, y, state):
        super().__init__(visible=False)
        self.penup()
        self.goto(x, y)
        self.write(state)
        home()
        self.score = 0

    def update_score(self, score):
        self.goto(0,350)
        self.write(f"Guessed states: {score}/50")
        self.score += 1
