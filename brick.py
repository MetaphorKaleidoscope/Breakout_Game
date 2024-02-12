from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color, points):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=2)
        self.goto(position)
        self.color(color)
        self.points = points
