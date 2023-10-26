from turtle import Screen, Turtle
from food import Food
from scoreboard import ScoreBoard
import snake
import time

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

# Setting up the Screen
s = Screen()
s.title(titlestring="Snake Game")
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()

# To control the Snake
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


def game_over():
    global game_is_on
    game_is_on = False
    over = Turtle()
    over.color("white")
    over.write(arg="Game Over", align=ALIGNMENT, font=FONT)


s.onkey(game_over, "space")
# To Move the Snake
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with the Food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()

    # Detect Collision with the Wall
    if (snake.head.xcor() > 290) or (snake.head.ycor() > 280) or (snake.head.xcor() < -290) or (
            snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect Collision with the Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

s.exitonclick()
