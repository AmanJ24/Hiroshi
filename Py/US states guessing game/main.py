import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.screensize(200, 200)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("50_states.csv")

is_game_on = True
Correct_count = 0

while is_game_on:
    answer = screen.textinput(f"{Correct_count}/50 States Guessed","What's another state's name")
    answer_state = answer.capitalize()

    if Correct_count < 50:
        for line in data.state:
            if answer_state in line:
                Correct_count += 1
                x_cor = int(data[data.state == answer_state].x)
                y_cor = int(data[data.state == answer_state].y)
                writer.goto(x_cor,y_cor)
                writer.write(answer_state)
            else:
                pass    
    else:
        is_game_on = False
        writer.goto(0,0)
        writer.write("You Win!!!", font = ["Arial", 20, "normal"])        

screen.exitonclick()