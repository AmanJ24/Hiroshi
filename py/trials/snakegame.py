from turtle import Turtle, Screen
import time 
import random 

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position, 0)
    
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(new_y, 0)

    def go_down(self):
        new_y = self.ycor() - 100
        self.goto(new_y, 0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.new_x = 10
        self.new_y = 10

    def move(self):
        new_x = self.xcor() + x_move
        new_y = self.ycor() + y_move
        self.goto(new_x, new_y)

screen = Screen()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()

screen.setup(800, 600)
screen.title("pong")
screen.bgcolor("black")
screen.tracer(0)




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()