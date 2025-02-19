#import all necessary libraries
import turtle


#create mason and screen obj
mason = turtle.Turtle()
screen = turtle.Screen()


#func that moves mason obj forward
def move_fd():
    mason.forward(10)

def move_bk():
    mason.back(10)

def turn_left():
    mason.setheading(mason.heading() + 10)

def turn_right():
    mason.setheading(mason.heading() - 10)


#activate user input
screen.listen()
#listen for user input and implement tank controls
screen.onkey(fun=move_fd, key='w')
screen.onkey(fun=move_bk, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
#clear drawing and reset turtle position
screen.onkey(fun=mason.reset, key='c')
#exit on click
screen.exitonclick()