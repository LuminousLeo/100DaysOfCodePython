#can create an alias for the classes and modules that i import
from turtle import Turtle as t, Screen as s
#can also import and install packages from the internet
#located in this website https://pypi.org/
import heroes

def main():
    #generate a random hero name
    print(heroes.gen())

    #creating Turtle obj
    mason = t()
    #set the shape of the timmy
    mason.shape('turtle')
    #change timmy's color
    #the color() method makes the obj black by default
    #for more info check this link https://docs.python.org/3/library/turtle.html#turtle.color
    #the hexes are in this link https://trinket.io/docs/colors
    mason.color('#FF8C00')
    #drawing a square with turtle graphics
    for i in range(15):
        mason.pendown()
        mason.forward(10)
        mason.penup()
        mason.forward(10)

    # creating Screen obj
    #put it at the end of the main file
    #or alternatively put it in another file
    screen = s()
    screen.exitonclick()



main()