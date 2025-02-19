#can create an alias for the classes and modules that i import
from turtle import Turtle as t, Screen as s, colormode
import random
#can also import and install packages from the internet
#located in this website https://pypi.org/

def main():
    #set the number of sides for all polygons
    triangle = 3
    square = 4
    pentagon = 5
    hexagon = 6
    heptagon = 7
    octagon = 8
    nonagon = 9
    decagon = 10

    # get the angles for all polygons
    triangle_angle = 360 / triangle
    square_angle = 360 / square
    pentagon_angle = 360 / pentagon
    hexagon_angle = 360 / hexagon
    heptagon_angle = 360 / heptagon
    octagon_angle = 360 / octagon
    nonagon_angle = 360 / nonagon
    decagon_angle = 360 / decagon

    #creating Turtle obj
    mason = t()
    #set mason's shape
    mason.shape('triangle')
    #set mason's speed
    mason.speed(10)

    # IMPORTANT NOTE!!!!!!
    #since the code is drawing multiple times, i could have
    #created a function like this
    #def draw_shape(sides, angle):
    #   for i in range(side):
            #mason.forward(100)
            #mason.right(angle)
    # END OF IMPORTANT NOTE!!!!!!

    # generate a random color
    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    #draw the triangle
    for i in range(triangle):
        #by default the pendown() method is on
        #meaning mason obj is going to draw a
        #line when it moves
        mason.forward(100)
        mason.right(triangle_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the square
    for i in range(square):
        mason.forward(100)
        mason.right(square_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the pentagon
    for i in range(pentagon):
        mason.forward(100)
        mason.right(pentagon_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the hexagon
    for i in range(hexagon):
        mason.forward(100)
        mason.right(hexagon_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the heptagon
    for i in range(heptagon):
        mason.forward(100)
        mason.right(heptagon_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the octagon
    for i in range(octagon):
        mason.forward(100)
        mason.right(octagon_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the nonagon
    for i in range(nonagon):
        mason.forward(100)
        mason.right(nonagon_angle)

    mason.color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    # draw the decagon
    for i in range(decagon):
        mason.forward(100)
        mason.right(decagon_angle)

    # creating Screen obj
    #put it at the end of the main file
    #or alternatively put it in another file
    screen = s()
    screen.exitonclick()



main()