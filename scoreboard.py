from turtle import Turtle

ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(position)
        self.hideturtle()
        self.refresh(self.score)

    def refresh(self, points):
        self.clear()
        self.score += points
        self.write(f'{self.score}', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))

    def game_over(self):
        self.goto(0, -50)
        self.write(f'GAME OVER ', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))
