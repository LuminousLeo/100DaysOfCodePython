# importing tkinter
import tkinter

def button_clicked():
    # get user input
    my_label.config(text=usr_input.get())


# creating and setting up a window for my program
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
# change the padding of the window
window.config(padx=20, pady=20)

# creating and writing a Label to the window
my_label = tkinter.Label(text='laliluleilou', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
# adding padding to the label
my_label.config(padx=20, pady=20)

# can also change the text in the label method this way
my_label['text'] = 'new text'
my_label.config(text='new text')

# creating a Button
button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)


# creating and Entry
usr_input = tkinter.Entry(width=25)
usr_input.grid(column=3, row=2)

# reminder that you cannot use pack(), place() and grid() methods
# in the same program. You have to choose one

new_button = tkinter.Button(text='Click me')
new_button.grid(column=2, row=0)



window.mainloop()