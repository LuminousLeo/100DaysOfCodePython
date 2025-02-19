from turtle import Turtle

class Scoreboard(Turtle):
    """Scoreboard() class, has all the necessary methods and
    fields to keep track of the score. Also inherits
    everything from the Turtle class"""

    def __init__(self):
        super().__init__()
        # inherit everything from the Turtle class
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.teleport(x=0, y=250)
        self.write(arg=f'Score: {self.score}' ,align='center', font=('Arial', 24, 'normal'))

    def score_increase(self, touching_food):
        """score_increase(touching_food) takes a boolean as an argument
        and if said boolean is true it increases the score"""
        if touching_food:
            self.clear()
            self.score += 1
            self.write(arg=f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))


    def game_over(self):
        """game_over() writes game over in the middle of the screen"""
        self.teleport(x=0, y=0)
        self.write(arg=f'Game Over', align='center', font=('Arial', 15, 'normal'))

