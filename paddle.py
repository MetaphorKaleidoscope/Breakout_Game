from turtle import Turtle

MOVE_DISTANCE = 70


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('#4281f5')
        self.shapesize(stretch_len=7, stretch_wid=0.5)
        self.goto(position)

    def right_move(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def left_move(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())
