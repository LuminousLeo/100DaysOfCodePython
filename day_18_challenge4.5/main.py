#can create an alias for the classes and modules that i import
from turtle import Turtle as t, Screen as s, colormode
import random
#can also import and install packages from the internet
#located in this website https://pypi.org/

def main():
    #change colormode from floats (0.00 to 1.0) to ints (0 to 255)
    colormode(255)

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


def random_color():
    #randomly generate rgb values
    r = random. randint(0, 255)
    g = random. randint(0, 255)
    b = random. randint(0, 255)

    #create a tuple containing the rgb value
    my_tuple = (r, g, b)

    return my_tuple


def random_walk(obj, angles):
    #set the color of the line
    #pass in a tuple as an argument for the pencolor method
    obj.pencolor(random_color())
    #way better than making the randomness my self
    #hehehehe ty python
    #better than the last design
    obj.setheading(random.choice(angles))
    obj.forward(30)


main()


