from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time


game_on = True

#create and set up screen obj
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

#create snake and food objs
snake = Snake()
food = Food()
scoreboard = Scoreboard()


#listen to user keystrokes
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')

while game_on:
    if snake.body_components[0].xcor() > 290 or snake.body_components[0].xcor() < -290:
        game_on = False
        scoreboard.game_over()

    if snake.body_components[0].ycor() > 290 or snake.body_components[0].ycor() < -290:
        game_on = False
        scoreboard.game_over()

    screen.update()
    food.score_up = False
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.body_components[0].distance(food) <= 19:
        food.score_up = True
        scoreboard.score_increase(touching_food=food.score_up)
        food.rand_location()
        snake.extend_snake()

    # collision with body
    for body_component in snake.body_components[1:]:
        if snake.body_components[0].distance(body_component) <= 15:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()