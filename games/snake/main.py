from turtle import Screen, Turtle
from snake import Snake
from border import Border
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=600, height=600)

#border
border = Border()
snake = Snake()

screen.listen()

up = screen.onkey(snake.up, "Up")
left = screen.onkey(snake.left, "Left")
right = screen.onkey(snake.right, "Right")
down = screen.onkey(snake.down, "Down")

food = Food()
score = Scoreboard()

end = Turtle(visible=False)
end.penup()
end.color("white")

SIZE = 273

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 25:
        food.refresh()
        screen.bgcolor("green")
        screen.bgcolor("black")
        score.food_eaten()
        snake.extend()

    if (
    snake.head.xcor() > SIZE - 20 or
    snake.head.xcor() < -SIZE + 20 or
    snake.head.ycor() > SIZE - 20 or
    snake.head.ycor() < -SIZE + 20
):
        game_over = end.write("Game Over")
        game_is_on = False


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = end.write("Game Over")
            game_is_on = False

    snake.move()




screen.exitonclick()
