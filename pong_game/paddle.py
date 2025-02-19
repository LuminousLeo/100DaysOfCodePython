from turtle import Turtle

UP_DIR = 90
DOWN_DIR = 270
MOVE_DISTANCE = 50


class Paddle(Turtle):
    """Paddle(start_x, start_y) class. takes in two ints has arguments. Inherits from Turtle class. Has
    all the necessary fields and methods to create and move a paddle"""

    def __init__(self, start_x, start_y):
        # inherit from Turtle() class
        super().__init__()

        # create the paddle and move it to the desired position
        self.shape(name='square')
        self.color('white')
        self.penup()
        self.resizemode(rmode='user')
        self.setheading(UP_DIR)
        self.shapesize(stretch_len=5)
        self.teleport(x=start_x, y= start_y)


    def move_up(self):
        """move_up() method, makes the paddle move upwards"""

        self.speed('fastest')
        self.setheading(UP_DIR)
        self.forward(MOVE_DISTANCE)


    def move_down(self):
        """move_down() method, makes the paddle move downwards"""

        self.speed('fastest')
        self.setheading(DOWN_DIR)
        self.speed('normal')
        self.forward(MOVE_DISTANCE)