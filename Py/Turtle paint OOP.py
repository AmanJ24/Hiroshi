import turtle as t
import random
timmy = t.Turtle()
timmy.color("red")
timmy.shape("turtle")

t.colormode(255)
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
  
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# colors = ["Blue", "Red", "Green", "Yellow", "brown", "magenta", "indigo", "maroon", "bisque", "deep sky blue"]
# n = 3
# for i in range(10):
#     if n <= 10:
#         for i in range(n):
#             timmy.right(360 / n)
#             timmy.forward(100)    
#         n += 1
#         timmy.color(random.choice(colors))

# timmy.pensize(8)
# timmy.speed("fastest")

# list1 = [0, 90, 180, 270]
# for i in range(100):
#     timmy.forward(30)
#     timmy.setheading(random.choice(list1))  
#     timmy.color(random_color())

timmy.speed("fastest")
def draw(size):
    for i in range(int(360 / size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)

draw(5)


screen = t.Screen()
screen.exitonclick()