from turtle import Turtle

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-230)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)