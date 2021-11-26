import random
from turtle import Turtle, colormode, exitonclick, Screen
import turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(3)

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

n=360
i=3
while i < 12:
    mov_tartaruga(i, n)
    i += 1
    turtle_color()


for move in range(50):
    n = random.choice(direction)
    i = random.randint(0,50)
    speed = random.randint(0,10)
    move_random(n, i, speed)
    random_color()

timmy.exitonclick()