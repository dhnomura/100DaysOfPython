from turtle import Screen, Turtle
import random
import time
from scoreboard import ScoreBoard

score = ScoreBoard()
RANDOM_DIRECTIONS=["west","east","northeast","southeast","northwest","southwest"]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(0,0)
        self.moviment = ["northeast","southeast","northwest","southwest"]
        self.direction = (random.choice(list(self.moviment)))


    def get_pos(self):
        return (self.pos())


    def move_ball(self):
        if (self.get_pos()[0]) < 400 or (self.get_pos()[0]) > -400:
            if self.direction == "northeast" and (self.get_pos()[1]<280):
                self.move_northeast()
            elif self.direction == "northeast" and (self.get_pos()[1]>270):
                self.direction = "southeast"
            if self.direction == "southeast" and (self.get_pos()[1]>-280):
                self.move_southeast()
            elif self.direction == "southeast" and (self.get_pos()[1]<270):
                self.direction = "northeast"
            if self.direction == "northwest" and (self.get_pos()[1]<280): 
                self.move_northwest()
            elif self.direction == "northwest" and (self.get_pos()[1]>270):
                self.direction = "southwest"
            if self.direction == "southwest" and (self.get_pos()[1]>-280):
                self.move_southwest()
            elif self.direction == "southwest" and (self.get_pos()[1]<270):
                self.direction = "northwest"
        elif (self.get_pos()[0]) > 400 or (self.get_pos()[0]) < -400:
            self.setpos(0,0)


    def bouce_2east(self):
        if self.direction == "northwest":
            self.direction = "northeast"
        elif self.direction == "southwest":
            self.direction = "southeast"

    def bouce_2west(self):
        if self.direction == "northeast":
            self.direction = "northwest"
        elif self.direction == "southeast":
            self.direction = "southwest"


    def restart_game(self,player):
        time.sleep(0.5)
        self.setpos(0,0)
        if player == "player1":
            self.direction = (random.choice(self.moviment))        
        if player == "player2":
            self.direction = (random.choice(self.moviment))


    def check_score(self):
        if self.direction == "northwest" or self.direction == "southwest":
        # if self.direction in ("northwest","southwest"):
            if (self.get_pos()[0]) < -400:
                self.player2 += 1
                self.restart_game("player2")
                score.increase_scorep2()
        elif self.direction == "northeast" or self.direction == "southeast":
            if (self.get_pos()[0]) > 400:
                self.player1 += 1
                self.restart_game("player1")
                score.increase_scorep1()


    def move_northeast(self):
        x = int(self.get_pos()[0]) + 10
        y = int(self.get_pos()[1]) + 10
        self.goto(x,y)
        self.check_score()


    def move_southeast(self):
        x = int(self.get_pos()[0]) + 10
        y = int(self.get_pos()[1]) - 10
        self.goto(x,y)
        self.check_score()


    def move_northwest(self):
        x = int(self.get_pos()[0]) - 10
        y = int(self.get_pos()[1]) + 10
        self.goto(x,y)
        self.check_score()


    def move_southwest(self):
        x = int(self.get_pos()[0]) - 10
        y = int(self.get_pos()[1]) - 10
        self.goto(x,y)
        self.check_score()

