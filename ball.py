from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("gray")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.goto(-400, -100)
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(-400, -100)
        self.bounce_y()

    def velocity(self):
        self.move_x += 1
        self.move_y += 1
