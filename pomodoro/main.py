import tkinter
from math import floor
from tkinter import Canvas

# ---------------------------- GLOBALS ------------------------------- #
timer_count = None
reps = None

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """reset_timer() resets the entire program"""

    global reps

    screen.after_cancel(timer_count)
    timer_txt.config(text='Timer', fg=GREEN)
    check_marks.config(text="")
    reps = None
    canvas.itemconfig(timer_countdown_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mechanism():
    """timer_mechanism() is the function that is called to call the timer()"""

    global reps
    # this try except block is used to check if it is the
    # first rep or not
    try:
        reps += 1
    except TypeError:
        reps = 1

    # variable to help with writing the checkmarks to the screen
    check_marks_num = int(reps / 2)

    # variables responsible for calculating the amount of seconds
    # to work, short rest and long rest
    work_timer = WORK_MIN * 60
    short_break_timer = SHORT_BREAK_MIN * 60
    long_break_timer = LONG_BREAK_MIN * 60

    # if else statement that checks to see if the
    # user should work, short rest or long rest
    # also ads the rep checkmarks to the screen
    if reps % 2 == 0 and reps != 8:
        timer_txt.config(text='Break', fg=PINK)
        timer(short_break_timer)
        check_marks.config(text=f"{CHECK_MARK}" * check_marks_num)
    elif reps % 2 == 0 and reps == 8:
        timer_txt.config(text='Break', fg=RED)
        check_marks.config(text=f"{CHECK_MARK}" * check_marks_num)
        timer(long_break_timer)
    else:
        timer_txt.config(text='Work', fg=GREEN)
        timer(work_timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    """timer(count) is the function that takes care of calculating how much time we have left
    and displays that time"""

    #conver the seconds to minutes
    minutes = floor(count / 60)
    #display the seconds correctly
    seconds = count % 60
    #this if else statement is used to check when the prog needs to place an additional 0
    if seconds == 0:
        canvas.itemconfig(timer_countdown_text, text=f"{minutes}:{seconds}0")
    elif 0 < seconds < 10:
        canvas.itemconfig(timer_countdown_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_countdown_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_count
        timer_count = screen.after(5, timer, count - 1)
    else:
        timer_mechanism()

# ---------------------------- UI SETUP ------------------------------- #
# creating and setting up the screen
screen = tkinter.Tk()
screen.title('Pomodoro')
screen.config(padx=100, pady=50, bg=YELLOW)

# setting up the 'Timer' text above the tomato image
timer_txt = tkinter.Label(text='Timer', font=(FONT_NAME, 45, 'bold'), foreground=GREEN, background=YELLOW)
timer_txt.grid(column=1, row=0)

# setting up the background image using Canvas() method from tkinter
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# getting the tomato image file
tomato_img = tkinter.PhotoImage(file='tomato.png')
# putting that image to the screen
canvas.create_image(100, 112, image=tomato_img)
# adding text to the screen
timer_countdown_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# creating and setting up the 'Start' and 'Reset' buttons
start_btn = tkinter.Button(text='Start', font=(FONT_NAME, 12, 'bold'), background=GREEN, command=timer_mechanism)
start_btn.grid(column=0, row=2)

start_btn = tkinter.Button(text='Reset' ,font=(FONT_NAME, 12, 'bold'), background=RED, command=reset_timer)
start_btn.grid(column=2, row=2)

# creating the check mark for the amount of times
# that the pomodoro has been used in the specific session
check_marks = tkinter.Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 12))
check_marks.grid(column=1, row=3)


screen.mainloop()