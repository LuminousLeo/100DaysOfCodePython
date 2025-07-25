################## IMPORTS/MODULES ##################
import database
import tkinter

################## CONSTANTS ##################
BACKGROUND_COLOR = '#B1DDC6'
FLASH_CARD_BACK_COLOR = '#91c2af'
WHITE = '#FFFFFF'
BLACK = '#000000'
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
JAP_LABEL_X = 280
JAP_LABEL_Y = 150
JAP_WORD_Y = 263
JAP_PRONOUNCE_Y = 363

################## CONNECT/CREATE DATABASE ##################
database.database_creation()

################## GLOBALS ##################
LIST_OF_WORDS = database.rand_words()

################## NEW WORDS ##################
def word_iter():
    """word_iter() is a function that changes
    the japanese word (and it's pronounciation and translation)
    that is being displayed on the screen. Also changes the current flash card image
    to the car_front.png"""

    LIST_OF_WORDS.pop(0)
    canvas.itemconfig(canvas_image, image=flash_card_front)
    curr_lang_indication.config(text='Japanese', bg=WHITE, fg=BLACK)
    try:
        curr_word.config(text=f'{LIST_OF_WORDS[0][0]}', bg=WHITE, fg=BLACK, font=('Ariel', 60, 'bold'))
    except IndexError:
        curr_lang_indication.config(text='You have learned 10 words today :)', bg=WHITE, fg=BLACK, font=('Ariel',30, 'italic'))
        curr_lang_indication.place(x=60, y=JAP_LABEL_Y)
        jap_pronounce.config(text='', bg=WHITE)
        curr_word.config(text='', bg=WHITE)
    else:
        jap_pronounce.config(bg=WHITE)
        jap_pronounce.config(text=f'({LIST_OF_WORDS[0][1]})')
        timer()

################## FLIP CARD ##################
def flip_card():
    """flip_card() is a function that flips the card to the card_back.png image
    and displays the translation for the current japanese word"""
    word_printed = ''
    canvas.itemconfig(canvas_image, image=flash_card_back)
    curr_lang_indication.config(text='English', bg=FLASH_CARD_BACK_COLOR, highlightthickness=0, fg=WHITE)
    for char in LIST_OF_WORDS[0][2]:
        if char == ',':
            word_printed += f'{char}\n'
        elif char == ')':
            word_printed += f'{char}\n'
        else:
            word_printed += f'{char}'

    curr_word.config(text=f'{word_printed}', bg=FLASH_CARD_BACK_COLOR, fg=WHITE, font=('Ariel', 30, 'bold'))
    jap_pronounce.config(text='', bg=FLASH_CARD_BACK_COLOR)

################## TIMER ##################
def timer():
    """timer() is a function that simply calls another function
    called flip_card() after 3 seconds"""
    window.after(ms=3000, func=flip_card)

################## SAVE WORDS/DON'T SAVE WORDS ##################
def save_words():
    """save_words() is a function  that calls upon the save_word_db() method from the database module
    and saves the word if the user guessed correctly"""
    database.save_word_db(LIST_OF_WORDS[0][0])
    word_iter()

def wrong_btn():
    """wrong_btn() is a function that simply calls the word_iter() function if
    the user clicked the 'wrong button' """
    word_iter()

################## UI ##################
# create window
window = tkinter.Tk()
window.title('Japanese Flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# set up the canvas with the first flash card image
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = tkinter.PhotoImage(file='./images/card_front.png')
flash_card_back = tkinter.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=flash_card_front)
canvas.grid(column=0, row=0, columnspan=2)

# display that the current word is in japanese
curr_lang_indication = tkinter.Label(text=f'Japanese', font=('Ariel',40, 'italic'), bg=WHITE, highlightthickness=0, fg=BLACK)
curr_lang_indication.place(x=JAP_LABEL_X, y= JAP_LABEL_Y)

# display japanese word
curr_word = tkinter.Label(text=f'{LIST_OF_WORDS[0][0]}', font=('Ariel', 60, 'bold'), bg=WHITE, highlightthickness=0, fg=BLACK)
curr_word.place(x=280, y=JAP_WORD_Y)

# display japanese word's pronounciation
jap_pronounce = tkinter.Label(text=f'({LIST_OF_WORDS[0][1]})', font=('Ariel', 30, 'bold'), bg=WHITE, highlightthickness=0, fg=BLACK)
jap_pronounce.place(x=280, y=JAP_PRONOUNCE_Y)

# display the 'right' button with the correct image
right_img = tkinter.PhotoImage(file='./images/right.png')
right_btn = tkinter.Button(image=right_img, background=BACKGROUND_COLOR, borderwidth=0, command=save_words)
right_btn.grid(column=1, row=1)

# display the 'wrong' button with the correct image
wrong_img = tkinter.PhotoImage(file='./images/wrong.png')
wrong_btn = tkinter.Button(image=wrong_img, background=BACKGROUND_COLOR, borderwidth=0, command=wrong_btn)
wrong_btn.grid(column=0, row=1)

timer()


window.mainloop()