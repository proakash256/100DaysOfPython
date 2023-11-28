from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_timer(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_timer(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_timer(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_timer(seconds):
    global timer
    count_minutes = seconds // 60
    count_seconds = seconds % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if seconds > 0:
        timer = window.after(1000, count_timer, (seconds - 1))
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_label.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
