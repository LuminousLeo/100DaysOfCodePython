import turtle
from paddle import Paddle
from opponent import Opponent
from ball import Ball
from scoreboard import Scoreboard

# CONST vars  from the user  and opponent starting pos, and height and width values for the screen
USER_X = 350
OPPONENT_X = -350
WIDTH = 800
HEIGHT = 600

# initialize the screen, user, opponent and ball objects
screen = turtle.Screen()
user = Paddle(start_x=USER_X, start_y=0)
opponent = Opponent(start_x=OPPONENT_X, start_y=0)
ball = Ball()
scoreboard = Scoreboard()

#set up the screen
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Pong')

#  boolean to help with game loop
game_is_on = True

# start listening to user input
screen.listen()

# loop for the game
while game_is_on:
    screen.update()

    if ball.xcor() >= WIDTH / 2:
        ball.teleport(x=0, y=0)
        ball.paddle_bounce()
        scoreboard.l_update()
    elif ball.xcor() <= -WIDTH / 2:
        ball.teleport(x=0, y=0)
        ball.paddle_bounce()
        scoreboard.r_update()
    else:
        ball.ball_move(HEIGHT / 2)

    # collision with right paddle
    if ball.xcor() >= 330 and ball.distance(user) <= 50:
        ball.paddle_bounce()
        ball.distance_x += 5

    # collision with left paddle
    if ball.xcor() >= -330 and ball.distance(opponent) <= 50:
        ball.paddle_bounce()
        ball.distance_x += 5


    # user and opponent keybinds and what they do
    screen.onkey(fun=user.move_up, key='Up')
    screen.onkey(fun=user.move_down, key='Down')
    screen.onkey(fun=opponent.move_up, key='w')
    screen.onkey(fun=opponent.move_down, key='s')

screen.exitonclick()