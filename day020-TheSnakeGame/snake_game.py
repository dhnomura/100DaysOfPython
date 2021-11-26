from turtle import Screen, screensize
from turtle import Turtle
import random
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)



# # screen.tracer(0)
# game_is_on = True
# snake_body = []
# bugs_name = []
# snake_id = 0
# counter = 0
# w = 0
# h = 0

# bug_w = random.randrange(-280, 280, 20)
# bug_h = random.randrange(-280, 280, 20)


# def check_catch(w, h):
#     global bug_w
#     global bug_h
#     global counter
#     global bugs_name
#     global snake_body
#     if w == bug_w and h == bug_h:
#         counter += 1
#         bug = bugs_name[0]
#         bug.reset()
#         del bugs_name[0]
#         new_bug()
#         growth_snake()


# def new_bug():
#     global bug_w
#     global bug_h
#     bug_w = random.randrange(-280, 280, 20)
#     bug_h = random.randrange(-280, 280, 20)
#     bug = Turtle(shape="turtle", visible=False)
#     bug.penup()
#     bug.shapesize(1)
#     bug.color("white")
#     bug.setpos(bug_w,bug_h)
#     bug.showturtle()
#     bugs_name.append(bug)
#     screen.update


# def growth_snake():
#     global snake_body
#     global w
#     global h
#     n = Turtle(shape="square")
#     n.hideturtle
#     n.color("white")
#     n.penup()
#     n.setpos(w,h)
#     bug_w = random.randrange(-280, 280, 20)
#     bug_h = random.randrange(-280, 280, 20)
#     n.showturtle()
#     snake_body.append(n)
#     screen.update


# def move_snake(snake,w,h):
#     snake.goto(w,h)
#     check_catch(w, h)


# def start_game():
#     global snake_body
#     for n in range(3):
#         n = Turtle(shape="square")
#         n.color("white")
#         n.penup()
#         snake_body.append(n)
#     # move_right()


# def move_right():
#     global w
#     global h
#     global game_is_on
#     global snake_body
#     while w < 290:
#         for snake_id in snake_body:
#             snake = snake_id
#             move_snake(snake,w,h)
#             check_catch(w, h)
#         w += 20
#     if w == 290:
#         game_is_on = False

# def move_left():
#     global w
#     global h
#     global game_is_on
#     global snake_body
#     while w > -290:
#         for snake_id in snake_body:
#             snake = snake_id
#             move_snake(snake,w,h)
#             check_catch(w, h)
#         w -= 20
#     if w == -290:
#         game_is_on = False


# def move_up():
#     global w
#     global h
#     global game_is_on
#     global snake_body 
#     while h < 290:
#         for snake_id in snake_body:
#             snake = snake_id
#             move_snake(snake,w,h)
#             check_catch(w, h)
#         h += 20
#     if h == 290:
#         game_is_on = False


# def move_down():
#     global w
#     global h
#     global game_is_on
#     global snake_body
#     while h > -290:
#         for snake_id in snake_body:
#             snake = snake_id
#             move_snake(snake,w,h)
#             check_catch(w, h)
#         h -= 20
#     if h == -290:
#         game_is_on = False


# screen.onkey(key="w", fun=move_up)
# screen.onkey(key="s", fun=move_down)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)


# start_game()
# new_bug()
# screen.listen()

# # while game_is_on:    

# # for n in range(0,-60,-20):
# #     snake=snake_body[snake_id]
# #     snake.goto(n,0)
# #     snake_id += 1

screen.exitonclick()
