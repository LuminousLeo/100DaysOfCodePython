# ------------------- IMPORTANT# ------------------- #
# i could not get the code for the ui/ux to work like
# it was shown in the tutorial, so I took some liberties with the code
# I hope it serves the same purpose

# --------------------------- LIBRARIES AND MODULES --------------------------- #
import tkinter
from tkinter import messagebox
import password_gen


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    """pass_gen() is a function that deletes the current in the password entry (input box)
    and then generates a new random password by calling the password_generator() function
    inside the password_gen module. Also copies generated password into clipboard"""
    password_input.delete(first=0, last=len(password_input.get()))
    password_input.insert(index=0, string=password_gen.password_generator())

# ---------------------------- Globals ------------------------------- #
WHITE = "#FFFFFF"
BLUE = "#0394fc"
GREY = "#b3b3b3"

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """save_data(), is a function that saves the the inputs in the website entry,
    email entry and password entry, in that order, into a txt file. The content of that file would look
    like this: something.com | something@gmail.com | something.
    It also checks if one of the entries is left blank (warns the user that they left one
    of them blank) and also ask if the user if they are sure they want to save the
    data inputted. Also created the data.txt file if it does not exist already."""
    website_data = website_input.get()
    email_data = email_username_input.get()
    password_data = password_input.get()

    data_string = f"{website_data} | {email_data} | {password_data}\n"

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        empty_warning  = messagebox.showwarning(title='Empty Fields', message='Some field were left empty.')
    else:
        save_checker = messagebox.askokcancel(title=website_data, message=f'These are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nDo you want to save?')

        if save_checker:
            with open('data.txt', 'a') as data_file:
                data_file.write(data_string)

            website_input.delete(first=0, last=len(website_data))
            password_input.delete(first=0, last=len(password_data))


# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = tkinter.Tk()
window.title('MyPass')
window.config(padx=20, pady=20)

# setting up the background image using Canvas() method from tkinter
canvas = tkinter.Canvas(width=200, height=200)
# getting the logo.png image file
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
# displaying logo.png on screen
canvas.grid(column=1, row=0)

# website label and entry
website = tkinter.Label(text="Website:")
website.grid(column=0, row=1)
website_input = tkinter.Entry(width=60, highlightthickness=1, highlightcolor=BLUE)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, pady=2)

# email/username label and entry
email_username = tkinter.Label(text="Email/Username:")
email_username.grid(column=0, row=2)
email_username_input = tkinter.Entry(width=60, highlightthickness=1, highlightcolor=BLUE)
email_username_input.insert(index=0, string="Dummy@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2, pady=2)

# password label, entry and buttons
password = tkinter.Label(text="password:")
password.grid(column=0, row=3)
password_input = tkinter.Entry(width=41, highlightthickness=1, highlightcolor=BLUE)
password_input.grid(column=1, row=3)
password_btn = tkinter.Button(text="Generate Password", command=pass_gen)
password_btn.grid(column=2, row=3, pady=2)

# add button
add_btn = tkinter.Button(text="Add", width=25, bg=BLUE, command=save_data)
add_btn.grid(column=1, row=4)


window.mainloop()