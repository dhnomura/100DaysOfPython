from turtle import Turtle, Screen
import turtle
from turtle import Turtle, Screen
import heroes

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

n=0
while n < 4:
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    n += 1
    
for m in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

for m in range(50):
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(10)
    timmy_the_turtle.color("white","red")
    timmy_the_turtle.forward(10)

timmy_the_turtle.forward(10)
timmy_the_turtle.tilt(360/4)
timmy_the_turtle.forward(10)


turtle.color("black", "red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.exitonclick()
