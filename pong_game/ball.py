from turtle import Turtle
import random

class Ball(Turtle):
    """Ball() class"""

    def __init__(self):

        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')

        self.bounce_down = False
        self.bounce_up = True
        self.distance_x = 20

    def ball_move(self, height):
        new_x = self.xcor() + self.distance_x
        if self.ycor() >= height - 10:
            self.bounce_down = True
            self.bounce_up = False
        if self.ycor() <= -height + 10:
            self.bounce_down = False
            self.bounce_up = True

        if self.bounce_up:
            new_y = self.ycor() + 15
        else:
            new_y = self.ycor() - 15

        self.goto(x=new_x, y=new_y)

    def paddle_bounce(self):
        self.distance_x *= -1
