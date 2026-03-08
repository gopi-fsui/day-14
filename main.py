from turtle import Screen
from backGround import BackGround
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000,height=700)
screen.title("My pong game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
AREA_X = 800 #actual width is 600
AREA_Y = 480 #actual height is 400


bg_w_line = BackGround(AREA_X,AREA_Y,"skyblue",True)

paddle_left = Paddle(int(-AREA_X/2)+20,AREA_Y)
paddle_right = Paddle(int(AREA_X/2)-20,AREA_Y)

ball = Ball(AREA_Y)



screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.start_pos()
    while not (abs(ball.xcor()) > AREA_X/2 or abs(ball.ycor()) > AREA_Y/2):
        screen.update()
        time.sleep(0.01)
        ball.move()


screen.mainloop()
