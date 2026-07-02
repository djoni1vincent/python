from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.counter = 0
        for car in range(6):
            self.create_car()
            self.car.goto(random.randint(-350,350), random.randint(-250, 250))


    def create_car(self):
        self.car = Turtle("square")
        self.car.penup()
        self.car.shapesize(stretch_len=3, stretch_wid=1)
        self.car.color(random.choice(COLORS))
        self.car.goto(random.randint(350,550), random.randint(-250, 250))
        self.cars.append(self.car)

    def move(self):
        for car in self.cars:
            car.fd(-4)

    def random_crate_car(self):
        self.counter += 1
        if self.counter % 10 == 0:
            self.create_car()
