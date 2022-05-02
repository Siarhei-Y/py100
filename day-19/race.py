from turtle import Turtle, Screen
import random
import turtle

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []


y = -90
for t in colors:
    tim = Turtle(shape="turtle")
    tim.color(t)
    tim.penup()
    y += 30
    tim.goto(x=-230, y=y)
    all_turtles.append(tim)
    


if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('WIN')
            else:
                print(f"LOST")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()