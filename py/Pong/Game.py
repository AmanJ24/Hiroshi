from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line

import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
middle = Line()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

middle.line()
while is_game_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y() 

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position() 
        score.r_point()   





screen.exitonclick()