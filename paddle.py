from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,start_pos_x,height):
        super().__init__("square")
        self.half_height = height/2
        self.color("black")
        self.shapesize(0.5,3,1)
        self.penup()
        self.goto(start_pos_x,0)
        self.setheading(90)
        # self.speed(0)
        # print("created")

    def move_up(self):
        if  self.ycor() < self.half_height-30:
            self.fd(30)

    def move_down(self):
        if  self.ycor() > -(self.half_height-30):
            self.bk(30)

