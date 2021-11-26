from turtle import Turtle, TurtleScreen
from turtle import Screen

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
