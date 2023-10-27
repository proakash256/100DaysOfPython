from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Constants
LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)

LEFT_SCORE_POSITION = (-100, 200)
RIGHT_SCORE_POSITION = (100, 200)

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)

l_paddle = Paddle(LEFT_PADDLE_POSITION)
r_paddle = Paddle(RIGHT_PADDLE_POSITION)
ball = Ball()
l_score = ScoreBoard(LEFT_SCORE_POSITION)
r_score = ScoreBoard(RIGHT_SCORE_POSITION)
game_is_on = True

# To control the Paddles
s.listen()

s.onkey(l_paddle.up, "w")
s.onkey(l_paddle.down, "s")

s.onkey(r_paddle.up, "Up")
s.onkey(r_paddle.down, "Down")


def game_over():
    global game_is_on
    game_is_on = False
    over = Turtle()
    over.color("white")
    over.write(arg="Game Over", align=ALIGNMENT, font=FONT)


s.onkey(game_over, "space")

while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detecting the collision with the Wall
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    # Detecting the collision with the Paddles

    # For Right Paddle
    if (ball.distance(r_paddle) < 50) and (ball.xcor() > 320):
        ball.bounce_x()

    # For Left Paddle
    if (ball.distance(l_paddle) < 50) and (ball.xcor() < -320):
        ball.bounce_x()

    # Detecting if the ball goes out of Bounds

    # For Right Paddle
    if ball.xcor() > 380:
        l_score.increase_score()
        ball.restart()

    # For Left Paddle
    if ball.xcor() < -380:
        r_score.increase_score()
        ball.restart()

s.exitonclick()
