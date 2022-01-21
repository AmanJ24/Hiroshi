from turtle import Screen, Turtle
from datetime import date, datetime, time, timedelta

dt = datetime.combine(date.today(), time(23, 55)) + timedelta(minutes=30)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
positions = [0, -20, -40]

segments = []

for i in range(0, 3):
    snake = Turtle(shape = "square")
    snake.color("white")
    snake.penup()
    snake.setposition(x = positions[i], y = 0)
    segments.append(snake)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(0.1) * dt
        screen.update()


screen.exitonclick()