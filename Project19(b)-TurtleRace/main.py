import random
from turtle import Turtle, Screen

s = Screen()
s.setup(width=500, height=400)

guess = s.textinput(title="Make Your Bet!", prompt="Enter the Colour of the turtle which you think will win!!")
colors = ["red", "orange", "green", "yellow", "blue", "purple", "black"]
turtles = []
is_race_on = False
y_pos = -150

for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 50

if guess:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f"Congratulations!! {guess} has won the Race.")
            else:
                print(f"Sorry!! {winning_color} has won the Race and {guess} has lost.")
        turtle.forward(random.randint(0, 10))
s.exitonclick()
