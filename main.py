# Breakout Game
from turtle import Screen
from wall import Wall
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from lives import Lives
import time

screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor("black")  # background color
screen.title("Breakout Game")
screen.tracer(0)  # Animation turn on

# make a wall
wall = Wall()
wall.build_wall()

paddle = Paddle((0, -200))
ball = Ball()

# scorebard
scoreboard = Scoreboard((470, 225))
# Lives
lives = Lives((-470, 225))

screen.listen()
screen.onkey(paddle.right_move, 'Right')
screen.onkey(paddle.left_move, 'Left')

game_is_on = True
while game_is_on:

    # Game over Lives end
    if lives.live < 0:
        scoreboard.game_over()
        game_is_on = False

    screen.update()  # Update all of screen and showed faster
    time.sleep(0.05)

    ball.move()

    # Detect collision with wall and bounce
    if ball.xcor() > 470 or ball.xcor() < -470:
        ball.bounce_x()
    if ball.ycor() > 230:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() <= -180:
        ball.bounce_y()
        ball.velocity()

    # Detect collision with bricks
    for brick_wall in wall.complete_wall:
        if ball.distance(brick_wall) < 50:
            dir(brick_wall)
            points = getattr(brick_wall, 'points')
            scoreboard.refresh(points)
            brick_wall.goto(-3000, -3000)
            ball.bounce_y()

    # Detect when paddle loss the ball
    if ball.ycor() < -230:
        lives.refresh()
        ball.reset_position()

screen.exitonclick()
