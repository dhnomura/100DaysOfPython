from turtle import Turtle, TurtleScreen
from turtle import Screen

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_fowards)

screen.exitonclick()
