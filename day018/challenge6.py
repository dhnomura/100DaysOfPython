import random
from turtle import Turtle, colormode, exitonclick, Screen, screensize
import turtle

timmy = Turtle()
timmy.shape("circle")
timmy.color("red")
timmy.pensize(2)

colors = ["red", "blue", "green", "black", "purple", "gray", "orange", "yellow"]
direction = [0, 90, 180, 270]

def mov_tartaruga(i, n):
    while n > 0:
        timmy.forward(30)
        n = n-(360/i)
        timmy.seth(n)

def move_random(n, i, speed):
    timmy.seth(n)
    timmy.forward(i)
    timmy.speed(speed)

def turtle_color():
    timmy.color(random.choice(colors))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    timmy.color(random_color)

for angle in range(0,360,10):
    timmy.seth(angle)
    timmy.circle(90, 360)
    speed = random.randint(0,10)
    turtle_color()

screen = turtle.Screen
screen.exitonclick()