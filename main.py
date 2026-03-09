from turtle import Screen,Turtle
from backGround import BackGround
from paddle import Paddle
from ball import Ball
from ScoreCard import ScoreCard
import time

screen = Screen()
screen.setup(width=1000,height=700)
screen.title("My pong game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
AREA_X = 800 #actual width is 600
AREA_Y = 400 #actual height is 400


bg_w_line = BackGround(AREA_X,AREA_Y,"skyblue",True)

paddle_left = Paddle(-int(AREA_X/2-20),AREA_Y)
paddle_right = Paddle(int(AREA_X/2-20),AREA_Y)

left_score = ScoreCard(-100,AREA_Y/2,"Left Score")
right_score = ScoreCard(100,AREA_Y/2,"Right Score")

ball = Ball(AREA_Y)

screen.update()

screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.start_pos()
    while abs(ball.xcor()) <= int(AREA_X/2)+20:
        screen.update()
        time.sleep(0.05)
        ball.move()
        if  abs(ball.ycor()) >= int(AREA_Y/2):
            ball.reflection()

        for left,right in zip(paddle_left.paddles_boxes,paddle_right.paddles_boxes):
            if int(left.distance(ball)) < 10 or int(right.distance(ball)) < 10:
                ball.paddle_ref()

    if  ball.xcor() < -300:
        right_score.score += 1
        right_score.update_score()

    elif ball.xcor() > 300:
        left_score.score += 1
        left_score.update_score()

    if left_score.score >= 10 or right_score.score >= 10:
        game_is_on = False


win_state = Turtle()
win_state.hideturtle()
win_state.color("red")
win_state.teleport(0,screen.window_height()/2 -50)


if left_score.score > right_score.score:
    win_state.write("Left Win!!",align="center",font=("arial",40,"bold"))
else:
    win_state.write("Right Win!!",align="center",font=("arial",40,"bold"))

screen.mainloop()

