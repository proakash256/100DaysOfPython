from tkinter import *
from tkinter import messagebox
import password_generator as pg
import pyperclip
import pandas

FONT = ("Tahoma", 10)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please enter the website name !")
        return
    found = False
    try:
        data = pandas.read_csv("data.csv")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found !!")

    else:
        for (index, row) in data.iterrows():
            if row.Name == website:
                found = True
                email = row.Email
                password = row.Password
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)
    finally:
        if not found:
            messagebox.showerror(title="Error", message=f"No details for {website} exist !!")
        website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def show_generated_password():
    generated_password = pg.generate_password()
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill all the Fields !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nSave the Details ?")
        if is_ok:
            new_data_dict = {"Name": [website], "Email": [email], "Password": [password]}
            new_data = pandas.DataFrame(new_data_dict)
            try:
                data = pandas.read_csv("data.csv")

            except FileNotFoundError or pandas.errors.EmptyDataError:
                new_data.to_csv("data.csv", index=False)

            else:
                website_list = data["Name"].to_list()
                if website in website_list:
                    index = website_list.index(website)
                    data.loc[index] = [website, email, password]
                    data.to_csv("data.csv", index=False)

                else:
                    new_data.to_csv("data.csv", mode='a', index=False, header=False)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", font=FONT, width=15, command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "proakash256@gmail.com")

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", font=FONT, width=16, command=show_generated_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", font=FONT, width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
