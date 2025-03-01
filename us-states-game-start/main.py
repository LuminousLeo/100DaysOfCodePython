import turtle
from string import capwords

from name import Name

# create and set up screen object
screen = turtle.Screen()
screen.title('U.S. States Games')
image = 'blank_states_img.gif'
screen.addshape(image)

# create name object
name = Name()

# boolean to help with game logic
game_on = True

# load desired image into the background
turtle.shape(image)

# loop to help with game logic
while game_on:
    # ask the user to type in the name of a state
    answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name? ")

    # check the state that the user inputted is in the states_dict
    name.state_checker(state=capwords(answer_state))



screen.exitonclick()