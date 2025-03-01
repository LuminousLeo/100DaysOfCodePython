import pandas
from turtle import Turtle

# font to be used when writing the state name in the map
FONT = ("Courier", 8, "normal")

# read the states csv file
DATA = pandas.read_csv('50_states.csv')

# create a list of all the states
STATES_DICT = list(DATA['state'])


class Name(Turtle):
    """Name() class, inherits form Turtle class and has the methods to
    check if the user guess is in the states dictionary and, if so, writes the name of the state
    in question in the correct location on the map"""

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color('black')
        print(STATES_DICT)


    def state_checker(self, state):

        if state in STATES_DICT:
            state_data = DATA[DATA['state'] == state]
            state_coord_tuple = (int(state_data['x']), int(state_data['y']))
            self.write_state(state=state ,coord_tuple=state_coord_tuple)


    def write_state(self, state, coord_tuple):
        self.goto(coord_tuple)
        self.write(arg=state, align='center', font=FONT)