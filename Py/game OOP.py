from turtle import Turtle, Screen
import random
screen = Screen()

# def move_forward():
#     tim.forward(15)

# def move_backward():
#     tim.backward(15)

# def move_left():
#     tim.left(15)

# def move_right():        
#     tim.right(15)

# def clear():
#     t.resetscreen()

# screen.listen()
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "a", fun = move_left)
# screen.onkey(key = "d", fun = move_right)
# screen.onkey(key = "c", fun = clear)

screen.setup(width = 500,height = 400) 
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")    

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()