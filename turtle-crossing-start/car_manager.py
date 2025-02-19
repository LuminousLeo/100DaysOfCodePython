from turtle import Turtle
import random

# constant variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
    """CarManager() class inherits from the Turtle class. It initializes the
    car object, sets it's heading to the north, selects a random color and teleports it to the bottom
    of the screen. It has the following methods: move(). It has the following fields: self.move_distance"""

    def __init__(self, starting_moving_distance):
        super().__init__()
        self.penup()
        self.setheading(to_angle=180)
        self.shape(name='square')
        self.resizemode(rmode='user')
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.teleport(x=360, y=random.randint(a=-250, b=250))

        self.move_distance = starting_moving_distance


    def move(self):
        """move() method moves the car forward by the field self.move_distance"""
        self.fd(self.move_distance)