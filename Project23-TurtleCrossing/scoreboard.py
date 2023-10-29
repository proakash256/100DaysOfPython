from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER !!", align="center", font=FONT)
