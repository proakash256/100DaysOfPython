from turtle import Turtle, Screen

tim = Turtle()
s = Screen()
s.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


s.onkey(move_forward, "w")
s.onkey(turn_left, "a")
s.onkey(move_backward, "s")
s.onkey(turn_right, "d")
s.onkey(clear, "c")
s.exitonclick()
