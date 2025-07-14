# ------------------- IMPORTANT# ------------------- #
# i could not get the code for the ui/ux to work like
# it was shown in the tutorial, so I took some liberties with the code
# I hope it serves the same purpose

# --------------------------- LIBRARIES AND MODULES --------------------------- #
import tkinter
import password_gen
import data
from tkinter import messagebox

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
WIDTH, HEIGHT = 200, 200
BTN_WIDTH_1 = 14
BTN_WIDTH_2 = 25

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data.save_data(website_input=website_input, email_username_input=email_username_input, password_input=password_input)

# ---------------------------- SEARCH ------------------------------- #
def search():
    """This search() function shows warning windows according to 3 specific factors:
    1-if the data.json file does not exist, it warns the user about it and explains how to go about creating one
    2-if the website that the user is searching for is not in the file, it warns the user about it
    3-if the data.json file exists and the website that the user inputted is in the file than it gives a popup
    box with the website name, email and password used for login into that website"""

    website_key = website_input.get()

    website_info = data.find_password(website=website_key)
    if website_info == 2:
        messagebox.showwarning(title='No Data File Found', message='Add you first website, email and password combination to generate a data file!')
    else:
        try:
            website_list = [k for k, v in website_info.items() if k == website_key]
        except AttributeError:
            messagebox.showwarning(title='No Info Available!', message='No details for the website exists!')
        else:
            messagebox.showwarning(title=f'{website_key}', message=f'Email: {website_info[website_list[0]]['email']}\nPassword: {website_info[website_list[0]]['password']}')

# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = tkinter.Tk()
window.title('MyPass')
window.config(padx=20, pady=20)

# setting up the background image using Canvas() method from tkinter
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT)
# getting the logo.png image file
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
# displaying logo.png on screen
canvas.grid(column=1, row=0)

# website label and entry
website = tkinter.Label(text="Website:")
website.grid(column=0, row=1)
website_input = tkinter.Entry(width=41, highlightthickness=1, highlightcolor=BLUE)
website_input.focus()
website_input.grid(column=1, row=1, pady=2)

# search button
search_btn = tkinter.Button(text="Search Info", bg=BLUE, width=BTN_WIDTH_1, command=search)
search_btn.grid(column=2, row=1, pady=2)

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
password_btn = tkinter.Button(text="Generate Password", command=pass_gen, width=BTN_WIDTH_1)
password_btn.grid(column=2, row=3, pady=2)

# add button
add_btn = tkinter.Button(text="Add", width=BTN_WIDTH_2, bg=BLUE, command=save)
add_btn.grid(column=1, row=4)


window.mainloop()