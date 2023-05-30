from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Score
import time

screen = Screen()

screen.title('The Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

r_pong = Pong((350, 0))
l_pong = Pong((-350, 0))
l_score = Score((-80, 180))
r_score = Score((80, 180))
ball = Ball()

screen.listen()

screen.onkeypress(r_pong.up, 'Up')
screen.onkeyrelease(r_pong.stop_move, 'Up')
screen.onkeypress(r_pong.down, 'Down')
screen.onkeyrelease(r_pong.stop_move, 'Down')
screen.onkeypress(l_pong.up, 'w')
screen.onkeyrelease(l_pong.stop_move, 'w')
screen.onkeypress(l_pong.down, 's')
screen.onkeyrelease(l_pong.stop_move, 's')


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pong) < 70 and ball.xcor() > 320 or ball.distance(l_pong) < 70 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed()

    if ball.xcor() > 380:
        l_score.score_up()
        ball.reset_position()

    if ball.xcor() < -380:
        r_score.score_up()
        ball.reset_position()


screen.exitonclick()