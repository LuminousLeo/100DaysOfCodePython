# import tkinter library
import tkinter
from idlelib.configdialog import font_sample_text


# function that converts miles to km and displays it
# in the converted label
def convert():
    converted_result = '%.2f' % (float(usr_input.get()) * 1.609)
    converted.config(text=str(converted_result))


# creating and setting up a window for this program
screen = tkinter.Tk()
screen.title('Miles to Kilometers')
screen.minsize(width=150, height=150)
screen.config(padx=75, pady=75)

# creating and setting up 'equal' label
equal = tkinter.Label(text='is equal to', font=('Arial', 16))
equal.config(padx=5, pady=5)
equal.grid(column=0, row=1)

# creating an Entry where the user is going
# to input what is to be converted
usr_input = tkinter.Entry(width=12)
usr_input.grid(column=1, row=0)

# creating and setting up 'miles' label
miles = tkinter.Label(text='Miles', font=('Arial', 16))
miles.config(padx=5, pady=5)
miles.grid(column=2, row=0)

# creating and setting up 'km' label
miles = tkinter.Label(text='Kilometers', font=('Arial', 16))
miles.config(padx=5, pady=5)
miles.grid(column=2, row=1)

# creating and setting up 'calculate' button
calculate = tkinter.Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)


# creating and setting up 'converted' label
converted = tkinter.Label(text='0', font=('Arial', 16))
converted.config(padx=5, pady=5)
converted.grid(column=1, row=1)


screen.mainloop()