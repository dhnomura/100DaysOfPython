from turtle import Turtle, screensize, up, update
STARTING_POSITION = {
    "right": (350,0),
    "left": (-350,0)
    }
MOVE_DISTANCE = (20)
RIGHT=0
UP=90
LEFT=180
DOWN=270

class Padle:


    def __init__(self):
        self.segments = {
            }
        self.create_padle()


    def create_padle(self):
        for side in STARTING_POSITION:
            self.add_segment(side, STARTING_POSITION[side])


    def add_segment(self, side, position):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_wid=5, stretch_len=1)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments[side]=new_segment


    def move(self):
        self.forward(MOVE_DISTANCE)


    def get_pos(self,side):
        return int((self.segments[side].pos()[1]))


    def right_up(self):
        y = self.get_pos("right")
        y += 20
        if y < 250:
            self.segments["right"].goto(350,y)


    def right_down(self):
        y = self.get_pos("right")
        y -= 20
        if y > -250:
            self.segments["right"].goto(350,y)


    def left_up(self):
        y = self.get_pos("left")
        y += 20
        if y < 250:
            self.segments["left"].goto(-350,y)


    def left_down(self):
        y = self.get_pos("left")
        y -= 20
        if y > -250:
            self.segments["left"].goto(-350,y)
            