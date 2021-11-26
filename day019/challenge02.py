from turtle import Turtle, TurtleScreen, color
from turtle import Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

width=-230
height=-70

colors  = ["red", "blue", "green", "orange", "yellow", "purple"]
turtles = []

# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a color: ")

for n in range(6): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(width, height)
    height += 30
    turtles.append(new_turtle)

stop = False
while not stop:
    for turtle in turtles:
        rand_distance = random.randint(0,30)
        turtle.forward(rand_distance)
        if turtle.position()[0] > 230:
            stop=True



# timmy = Turtle(shape="turtle")
# tommy = Turtle(shape="turtle")
# jenny = Turtle(shape="turtle")
# Jonny = Turtle(shape="turtle")
# wally = Turtle(shape="turtle")
# wolly = Turtle(shape="turtle")

# timmy.color("green")


# timmy.penup()
# timmy.goto(-230, -100)

screen.exitonclick()
