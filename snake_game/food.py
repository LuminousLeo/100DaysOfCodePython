from turtle import Turtle
import random

class Food(Turtle):
    """Food() class, has all necessary
    methods and fields to initialize the food and move it
    to a random location. It also inherits from the Turtle class"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.rand_location()
        self.score_up = False


    def rand_location(self):
        rand_x = random.randint(a=-300 + 25, b=300 - 25)
        rand_y = random.randint(a=-300 + 25, b=300 - 25)
        self.teleport(rand_x, rand_y)