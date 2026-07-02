from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.penup()
        self.goto(-250, 300)
        self.write(f"Level: {self.level}")

    def new_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}")


    def game_over(self):
        self.level = 1
        self.home()
        self.write("GAME OVER.")

