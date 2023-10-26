import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
