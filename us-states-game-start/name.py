import pandas
from turtle import Turtle

# font to be used when writing the state name in the map
FONT = ("Courier", 8, "normal")

# read the states csv file
DATA = pandas.read_csv('50_states.csv')

# create a list of all the states
STATES = list(DATA['state'])


class Name(Turtle):
    """Name() class, inherits form Turtle class and has the methods to
    check if the user guess is in the states dictionary and, if so, writes the name of the state
    in question in the correct location on the map"""

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color('black')
        # states that the user has guessed
        self.correct_states = []
        # missing states
        self.missing_states = {
            'states to memorize': []
        }


    def state_checker(self, state):
        """state_checker(state) method takes in a string and
        checks if that string is a U.S state"""

        # if the state string is a U.S state
        if state in STATES:
            # get the state series
            state_data = DATA[DATA['state'] == state]
            # get the state coord
            state_coord_tuple = (int(state_data['x']), int(state_data['y']))
            # append the state to the correct_states list
            self.correct_states.append(state)
            # write the name of the state in the correct spot on the map
            self.write_state(state=state ,coord_tuple=state_coord_tuple)


    def write_state(self, state, coord_tuple):
        """write_state(state, coord_tuple) method, takes in a string and a tuple of ints. writes the string in the
        indicated location"""

        self.goto(coord_tuple)
        self.write(arg=state, align='center', font=FONT)


    def states_to_memorize(self):
        """states_to_memorize() method creates a csv file with names of the states
        that the user did not guess"""

        for state in STATES:
            if state not in self.correct_states:
                self.missing_states['states to memorize'].append(state)

        missing_states_data = pandas.DataFrame(data=self.missing_states)
        missing_states_data.to_csv('states_to_memorize.csv')