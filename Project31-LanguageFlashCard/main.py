import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    canvas.itemconfig(canvas_img, image=canvas_front_img)
    global current_card
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=canvas_back_img)

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    words_to_learn_data = pandas.DataFrame(to_learn)
    words_to_learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(width=800, height=526)

canvas_front_img = PhotoImage(file="images/card_front.png")
canvas_back_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 263, image=canvas_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Text", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, border=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, border=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
