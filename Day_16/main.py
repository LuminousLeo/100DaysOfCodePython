"""
#importing the module that we created
import another_module
#printing what is inside that module
#print an attribute
print(another_module.another_variable)

#importing turtle module
import turtle
#creating an object named timmy from turtle module from turtle class (object)
timmy = turtle.Turtle()
print(timmy)
#change the color of which timmy is displayed
timmy.color('OrangeRed1')
#this func (or method since it is from the object named timmy) changes
#the shape of timmy on the screen
timmy.shape('turtle')
#move timmy forward by 100 pixels
timmy.forward(100)

#creating an object named screen
my_screen = turtle.Screen()
#printing an attribute of the my_screen object
print(my_screen.canvheight)

#a func that is inside of an object is called a method
#this method closes the screen when you click on it
my_screen.exitonclick()
"""

#import pretty table class
from prettytable import PrettyTable

#creating an object named table from prettytable class that is inside prettytable module
table = PrettyTable()
#creating pokemon list
pokemon = ['Pikachu', 'Squirtle', 'Charmander']
#creating pokemon types list
pokemon_type = ['Electric', 'Water', 'Fire']
#use add_column method from table object
table.add_column('Pokemon', pokemon)
table.add_column('Type', pokemon_type)
#change table alignment
table.align = 'l'
#print table
print(table)