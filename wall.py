from turtle import Turtle
from brick import Brick


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.brick = Brick
        self.color_brick = ['GREEN', 'YELLOW', 'ORANGE', 'RED']
        self.x_position = -500
        self.y_position = 50
        self.step_x = 110
        self.step_y = 50
        self.complete_wall = []

    def build_wall(self):
        n = 1
        for color in self.color_brick:
            for _ in range(10):
                if color == 'GREEN':
                    points = 1
                elif color == 'YELLOW':
                    points = 3
                elif color == 'ORANGE':
                    points = 5
                else:
                    points = 7
                self.brick = Brick((self.x_position, self.y_position), color, points)
                self.complete_wall.append(self.brick)
                self.x_position += self.step_x
            self.y_position += self.step_y
            self.step_x *= -1
            if n % 2 != 0:
                self.x_position = 500
                n += 1
            else:
                self.x_position = -500
                n += 1
