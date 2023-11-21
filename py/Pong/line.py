from turtle import Turtle

class Line(Turtle):
    def line(self):
            self.goto(0, 300)
            self.hideturtle()
            self.setheading(270)
            for i in range(100):
                self.pendown()
                if i%3 == 0:
                    self.penup()
                self.forward(10)