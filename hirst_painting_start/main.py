#import colorgram library
#import colorgram
import turtle
import random

def main():
    #    get all rgb tuples from each color present in image.jpg as a list of objects
    #    hisrt_object_colors = colorgram.extract('image.jpg', 40)

    #    empty list where each item is going to be a tuple
    #    colors = []
    #
    #    for obj in hisrt_object_colors:
    #        r = obj.rgb.r
    #        g = obj.rgb.g
    #        b = obj.rgb.b
    #        color_tuple = (r, g, b)
    #        colors.append(color_tuple)
    #
    #    print(colors)

    #commented out everything above because it only needs to be done once

    #change color mode to 255

    #color list for the hirst painting that is to be painted
    #each item of the list is a tuple
    color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

    #initialize mason object
    mason = turtle.Turtle()
    #initialize screen object
    screen = turtle.Screen()

    #change color mode to 255
    screen.colormode(255)

    #set the diameter for each of the hirst spots
    CIRCLE_DIAMETER = 20


    #teleport mason obj to the initial location
    mason.teleport((-screen.window_width() / 2) + CIRCLE_DIAMETER, (-screen.window_height() / 2) + CIRCLE_DIAMETER)

    #speed things up
    mason.speed(10)

    # columns or y_pos
    for y_pos in range(10):

        # rows or x_pos
        mason.penup()
        for x_pos in range(10):
            mason.dot(CIRCLE_DIAMETER, random.choice(color_list))
            mason.forward(50)

        # give mason obj x,y coordinates
        mason.teleport((-screen.window_width() / 2) + CIRCLE_DIAMETER, mason.ycor() + CIRCLE_DIAMETER + 50)

    #hide turtle after completing the painting
    mason.hideturtle()


    screen.exitonclick()








main()