from tkinter import *

FONT = ("Arial", 15, "italic")

window = Tk()
window.title("Fahrenheit to Celsius Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input_fah = Entry(width=10)
input_fah.grid(row=0, column=1)

# # If we want to take the input using a Spinbox
# input_spinbox = Spinbox(from_=0, to=1000, width=10, command=fah_to_cel)
# input_spinbox.grid(row=0, column=1)

name_fah = Label(text="Fahrenheit", font=FONT)
name_fah.grid(row=0, column=2)
name_fah.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=10, pady=10)

output_cel = Label(text="", font=FONT)
output_cel.grid(row=1, column=1)
output_cel.config(padx=10, pady=10)

name_cel = Label(text="Celsius", font=FONT)
name_cel.grid(row=1, column=2)
name_cel.config(padx=10, pady=10)


def fah_to_cel():
    fah = float(input_fah.get())
    cel = round((fah - 32) / 1.8, 5)
    output_cel.config(text=f"{cel}")


calculate_button = Button(text="Calculate", command=fah_to_cel)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=10, pady=10)

window.mainloop()
