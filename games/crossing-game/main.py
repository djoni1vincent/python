import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from border import Border


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

border = Border()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

speed = 0.1
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.random_crate_car()
    car_manager.move()

    # Collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 35:
            scoreboard.game_over()
            car_manager.car.clear()
            game_is_on = False

    # Next level
    if player.ycor() > 260:
        player.goto(0, -280)
        scoreboard.new_level()
        speed *= 0.7



screen.exitonclick()
