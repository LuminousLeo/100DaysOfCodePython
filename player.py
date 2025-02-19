from turtle import Turtle

# constant variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player() class, inherits from Turtle from the turtle module."""

    def __init__(self):
        super().__init__()
        self.penup()
        # give the Player class a turtle shape
        self.shape(name='turtle')
        # make the Player face upwards
        self.setheading(to_angle=90)
        self.star_pos()


    def star_pos(self):
        # make the Player go to the starting position
        self.speed('fastest')
        self.goto(STARTING_POSITION)
        self.speed('normal')


    def move(self):
        """method used to move the player"""
        self.fd(MOVE_DISTANCE)

    def finish_line_check(self):

        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False