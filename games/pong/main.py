
import time
from turtle import Screen
from paddle import Paddle
from border_back import Border
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.bgcolor("purple")
screen.tracer(0)

border = Border()
ball = Ball()

paddle_left = Paddle(-440,0)
paddle_right = Paddle(440,0)

# move up and down, with w/s, and arrows
screen.listen()
up_l = screen.onkeypress(paddle_right.move_up, "Up")
down_l = screen.onkeypress(paddle_right.move_down, "Down")

up_r = screen.onkeypress(paddle_left.move_up, "w")
down_r = screen.onkeypress(paddle_left.move_down, "s")

score = Score()
speed = 0.07
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # Detect colision with wall
    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.bounce_y()

    # Detect colision with paddle
    if ball.distance(paddle_right) < 30 and ball.xcor() >= 400 or ball.distance(paddle_left) < 30 and ball.xcor() <= -400 :
        ball.bounce_x()
        speed *= 0.9


    if ball.xcor() > 440 :
        score.right_score()
        speed = 0.07
        ball.restart()

    if ball.xcor() < -440:
        score.left_score()
        speed = 0.07
        ball.restart()



screen.exitonclick()
