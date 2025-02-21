from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Налаштування екрану
screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Створення об'єктів
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Управління ракетками
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Основний цикл гри
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Відбивання від стін
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Відбивання від ракеток
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Оновлення рахунку
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()
