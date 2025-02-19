from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 0
        self.update_level()


    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-225, y=250)
        self.write(arg='Level: ', align='center', font=FONT)
        self.goto(x=-150, y=250)
        self.write(arg=self.level, align='center', font=FONT)


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='Game Over', align='center', font=FONT)


