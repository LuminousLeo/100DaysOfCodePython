import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# variables to help with car speed
# and their increase in speed
# moved them in out of the car_manager module
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
updated_moving_distance = STARTING_MOVE_DISTANCE

# create and set up the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create scoreboard object
scoreboard = Scoreboard()

# create the player object
player = Player()

# list of all the cars on screen
cars = []
# variable to help spawn cars
car_gen_helper = 0

#boolean to help with game loop
game_is_on = True

# start 'listening' to player input
screen.listen()

# while loop to help with game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create a new car object and append it to the cars list
    # every 6 iterations of the loop
    if car_gen_helper % 6 == 0:
        cars.append(CarManager(starting_moving_distance=updated_moving_distance))

    # loop through each of the car objects in the cars list
    for car in cars:
        # move the car object
        car.move()

        # check for collision between player and the current car object
        if player.distance(car) < 20:
            # if so quit of the loop and end game
            scoreboard.game_over()
            game_is_on = False

    if player.finish_line_check():
        scoreboard.update_level()
        player.star_pos()

        # only changes the speed of new car objects being created
        # I like this completely intended feature so I'm not changing it
        updated_moving_distance += MOVE_INCREMENT


    # keybindings
    screen.onkey(fun=player.move, key='Up')

    car_gen_helper += 1



screen.exitonclick()
