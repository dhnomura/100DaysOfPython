from turtle import Turtle
from turtle import Screen

ALIGMENT = "center"
FONT = ("Arial",32,"normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-360,260)
        self.update_score()
        self.goto(-100,200)
        self.write(self.player1, align=ALIGMENT, font = FONT)
        self.goto(100,200)
        self.write(self.player2, align=ALIGMENT, font = FONT)


    def increase_scorep1(self):
        self.player1 += 1
        self.clear()
        self.update_score()


    def increase_scorep2(self):
        self.player2 += 1
        self.clear()
        self.update_score()


    def update_score(self):
        self.goto(-100,200)
        self.write(self.player1, align=ALIGMENT, font = FONT)
        self.goto(100,200)
        self.write(self.player2, align=ALIGMENT, font = FONT)        


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)