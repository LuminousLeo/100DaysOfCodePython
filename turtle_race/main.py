#import all necessary libraries
import turtle
import random

def main():
    #create screen obj
    screen = turtle.Screen()
    # set screen size
    screen.setup(width=500, height=400)
    #set up a bool var to help who won the race
    race_is_on = True

    #create all turtle objs
    for l in range(6):
        turtle.Turtle(shape='turtle')
    #list of colors that are going to be used by the turtles
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    #list of all the turtles
    turtle_list = screen.turtles()

    #get user text input
    user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')

    #set up the variables for the starting coordinates and
    start_x = (-screen.window_width() / 2) + 20
    start_y = -100

    #change the color of all the turtles
    for i in range(len(turtle_list)):
        turtle_list[i].color(colors[i])

    #make the turtle objs not draw a line
    for x in screen.turtles():
        x.penup()

    #make all the turtles go to their starting positions
    for turtle_start_pos in turtle_list:
        turtle_start_pos.goto(x=start_x, y=start_y)
        start_y += 30

    #loop to help with the race
    while race_is_on:
        #loop through the entire list of turtles
        for n in range(len(turtle_list)):
            turtle_list[n].forward(random.randint(0, 10))

            #check if the current turtle has reached the edge of the window
            if turtle_list[n].xcor() >= (screen.window_width() / 2) - 30:
                #check if user has won
                if user_bet == colors[n]:
                    print(f'You won! The {colors[n]} turtle is the winner!')
                else:
                    print(f'You lost:( The {colors[n]} turtle is the winner!')
                race_is_on = False

    #exit on click
    screen.exitonclick()


main()