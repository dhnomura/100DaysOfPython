import colorgram
import random
from turtle import Turtle
from turtle import Screen


screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("circle")
timmy.color("white")
timmy.pensize(2)
timmy.speed(10)
timmy.pensize(0)
timmy.hideturtle()
timmy.penup()

colors = colorgram.extract('dots.jpg', 30)

def set_color():
    global colors
    n=random.randint(3,29)
    color = colors[n]
    rgb=color.rgb
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    timmy.color(r,b,b)
    timmy.dot(20,(r,b,b))

for ver in range(-200,200,40):
    for hor in range(-200,200,40): 
        timmy.setpos(hor,ver)
        set_color()
        timmy.stamp()

screen.exitonclick()

