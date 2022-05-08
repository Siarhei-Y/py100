import imp
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=275)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}',align='center', font=('Arial',15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align='center', font=('Arial',15, 'normal'))

    def add_point(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()