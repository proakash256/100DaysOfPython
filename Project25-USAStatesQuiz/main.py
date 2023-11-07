from turtle import Turtle, Screen
import pandas

# Constants
FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

# Setting up the Screen
screen = Screen()
screen.title("Guess the U.S. States")
screen.setup(width=729, height=491)
screen.bgpic(picname="blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_states = []
missed_states = []

game_is_on = True

while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Write the name of the State")
    answer = answer.title()
    if answer == "Exit":
        break
    if answer in states_list:
        guessed_states.append(answer)
        state_position = data[data["state"] == answer]
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(int(state_position["x"]), int(state_position["y"]))
        tim.write(arg=f"{answer}", align=ALIGNMENT, font=FONT)
    if len(guessed_states) == 50:
        game_is_on = False

missed_states = [state for state in states_list if state not in guessed_states]

for state in missed_states:
    state_position = data[data["state"] == state]
    tim = Turtle()
    tim.color("red")
    tim.penup()
    tim.hideturtle()
    tim.goto(int(state_position["x"]), int(state_position["y"]))
    tim.write(arg=f"{state}", align=ALIGNMENT, font=FONT)

states_to_learn = pandas.DataFrame(missed_states)
states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
