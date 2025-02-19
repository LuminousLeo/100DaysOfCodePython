#can create an alias for the classes and modules that i import
from turtle import Turtle as t, Screen as s, colormode
import random
#can also import and install packages from the internet
#located in this website https://pypi.org/

def main():
    #creating Turtle obj
    mason = t()
    #set mason's shape
    mason.shape('triangle')
    #set mason's speed
    mason.speed(10)
    #set the size of the line
    mason.pensize(5)

    #list of angles for east, north, south and west
    cardinal_directions = [0, 90, 180, 270]

    for i in range(100):
        random_walk(mason, cardinal_directions)



    # creating Screen obj
    #put it at the end of the main file
    #or alternatively put it in another file
    screen = s()
    screen.exitonclick()


def random_walk(obj, angles):
    turn = random.randint(0, 3)
    #move east
    if turn == 0:
        obj.setheading(angles[0])
        # set a random color every time it draws
        #a tuple
        #my_tuple = (1,2,3)
        #if i want to access the first item in the my_tuple var
        #i can do this my_tuple[0]
        # btw a tuple is set in stone (cannot be changed)
        #using a tuple to generate a random color for the pen
        obj.pencolor((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
        obj.forward(10)
    #move north
    elif turn == 1:
        obj.setheading(angles[1])
        # set a random color every time it draws
        obj.pencolor((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
        obj.forward(10)
    # move west
    elif turn == 2:
        obj.setheading(angles[2])
        # set a random color every time it draws
        obj.pencolor((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
        obj.forward(10)
    # move south
    elif turn == 1:
        obj.setheading(angles[3])
        # set a random color every time it draws
        obj.pencolor((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
        obj.forward(10)


main()


