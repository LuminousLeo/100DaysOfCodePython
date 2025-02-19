#import all necessary libraries
import turtle


def move_obj():
    mason.forward(10)

#create mason and screen obj
mason = turtle.Turtle()
screen = turtle.Screen()

#make the screen sensible to user input
screen.listen()

screen.onkey(fun=move_obj, key='space')


#exit on click
screen.exitonclick()
