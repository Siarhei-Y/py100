from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def bacwards():
    tim.forward(-10)

def left():
    tim.left(10)

def right():
    tim.right(10)


screen.listen()

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=bacwards)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)

screen.exitonclick()