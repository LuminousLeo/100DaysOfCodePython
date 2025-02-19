import turtle
from time import sleep

MOVE_DISTANCE = 20
START_X = 0
START_Y = 0

class Snake:
    """Snake() class, has all the methods and fields necessary
    to create the body of the snake, to add more body components, detect collision
    with its own body and the keybindings to move the snake around"""

    def __init__(self):
        """Snake(screen) creates the starting body for the snake
        and takes in the screen object"""

        #list of all the body components objs
        # self.body_components = screen.turtles()
        # NOTE: DID NOT USE THE screen.turtles() method
        # BECAUSE THE FOOD OBJ IS ALSO A TURTLE AND
        # IT WOULD JUST COMPLICATE MY LIFE IN THE FUTURE
        # WHEN I WOULD ADD MORE BODY COMPONENTS TO THE SNAKE
        # SO I'M GOING TO ADD THE COMPONENTS MANUALLY (AUTOMATED BUT YOU KNOW WHAT
        # I MEAN)

        # create the body of the snake (start)
        self.body_components = []

        # change the snake's body color,
        # align the body correctly
        # and set size of each body component
        self.start_x = START_X

        self.create_snake()



    def move(self):
        """move() method makes the snake move"""
        for body_component in range(len(self.body_components) - 1, 0, -1):
            new_x = self.body_components[body_component - 1].xcor()
            new_y = self.body_components[body_component - 1].ycor()
            self.body_components[body_component].teleport(x=new_x, y=new_y)

        #move the head of the snake
        self.body_components[0].forward(MOVE_DISTANCE)


    def create_snake(self):
        for i in range(3):
            self.body_components.append(turtle.Turtle(shape='square'))

        print(len(self.body_components))

        for body_component in self.body_components:
            body_component.color('white')
            body_component.teleport(x=self.start_x, y=START_Y)
            body_component.penup()
            self.start_x -= 20


    def extend_snake(self):
        self.body_components.append(turtle.Turtle(shape='square'))
        self.body_components[-1].color('white')
        self.body_components[len(self.body_components) - 1].penup()

        if self.body_components[-2].heading() == 0:
            self.body_components[-1].teleport(self.body_components[-2].xcor() - 20, self.body_components[-2].ycor())
        if self.body_components[len(self.body_components) - 2].heading() == 180:
            self.body_components[len(self.body_components) - 1].teleport(self.body_components[-2].xcor() + 20, self.body_components[-2].ycor())
        if self.body_components[len(self.body_components) - 2].heading() == 90:
            self.body_components[len(self.body_components) - 1].teleport(self.body_components[-2].xcor() ,self.body_components[-2].ycor() - 20)
        if self.body_components[len(self.body_components) - 2].heading() == 270:
            self.body_components[len(self.body_components) - 1].teleport(self.body_components[-2].xcor(), self.body_components[-2].ycor() + 20)


    def up(self):
        """up() makes the snake face north aka go up"""
        # snake cannot go into itself
        if self.body_components[0].heading() != 270:
            self.body_components[0].setheading(90)


    def left(self):
        """left() makes the snake face west aka go left"""
        # snake cannot go into itself
        if self.body_components[0].heading() != 0:
            self.body_components[0].setheading(180)


    def down(self):
        """left() makes the snake face south aka go down"""
        # snake cannot go into itself
        if self.body_components[0].heading() != 90:
            self.body_components[0].setheading(270)


    def right(self):
        """left() makes the snake face east aka go right"""
        # snake cannot go into itself
        if self.body_components[0].heading() != 180:
            self.body_components[0].setheading(0)