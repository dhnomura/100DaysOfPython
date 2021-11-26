from turtle import Turtle
from turtle import Screen
import turtle

ALIGMENT = "center"
FONT = ("Arial",24,"normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)