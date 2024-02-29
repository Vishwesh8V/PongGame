from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
pad1 = Paddle((370, 0))
pad2 = Paddle((-370, 0))
game_is_on = True

screen.listen()
screen.onkey(pad1.go_up, "Up")
screen.onkey(pad2.go_up, "w")
screen.onkey(pad1.go_down, "Down")
screen.onkey(pad2.go_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.xcor() > 340 and ball.distance(pad1) < 50) or (ball.xcor() < -340 and ball.distance(pad2) < 50):
        ball.collision()
    elif ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
