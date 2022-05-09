from os import sched_rr_get_interval
from turtle import Screen, Turtle, color
from timmy import Timmy


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor()
screen.tracer(0)


timmy = Timmy()
screen.listen()
screen.onkey(key='w', fun=timmy.move)



game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
