from turtle import Screen, left
from padle import Padle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
game_is_on = True
screen.tracer(0)

padles = Padle()
ball = Ball()
right_padle=padles.segments["right"]
left_padle=padles.segments["left"]

screen.listen()
screen.onkey(padles.right_up, "Up")
screen.onkey(padles.right_down, "Down")
screen.onkey(padles.left_up, "w")
screen.onkey(padles.left_down, "s")
screen.update()

a = ball.move_southwest

while game_is_on:
    ball.move_ball()
    screen.update()

    # Detect Collission
    if ball.distance(right_padle) < 50 and ball.xcor() > 320:
        ball.bouce_2west()
    if ball.distance(left_padle) < 50 and ball.xcor() < -320:
        ball.bouce_2east()

    time.sleep(0.1)

screen.exitonclick()