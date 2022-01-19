import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

tim.hideturtle()    
tim.speed("fastest")   
tim.setheading(215)
tim.penup()
for i in range(7):
    tim.forward(50)

def walk():
    tim.setheading(0)       
    for i in range(10):
        tim.forward(50)
        tim.dot(20, random_color())
    
    tim.left(90)
    tim.forward(50)
    tim.setheading(180)

    for i in range(10):
        tim.forward(50)

for i in range(10):
    walk()    

   

screen = t.Screen()
screen.exitonclick()