# Damien Hirst is painter who has made many spot paintings which are being sold for millions of dollars.
# In this project we generate our own hirst like painting.

import turtle
from colors import color_list
import random

turtle.colormode(255)
tim = turtle.Turtle()
screen = turtle.Screen()

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dots in range(1, (no_of_dots + 1)):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
