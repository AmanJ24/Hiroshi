import turtle
import pandas

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
screen = turtle.Screen()
screen.title("US States Game")

image = "blank_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput("Guess the State","What's another state's name")
print(answer_state)

for line in data:
    if answer_state in line:
        print("its here")



screen.exitonclick()