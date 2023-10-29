from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.color("black")
        self.go_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
