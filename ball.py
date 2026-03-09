from turtle import Turtle
import random

ANGLE = [0,30,150,180,210,330]

class Ball(Turtle):
    def __init__(self,height:int):
        super().__init__("circle")
        self.half_height = int(height/2)
        self.color("black")
        self.penup()
        self.shapesize(0.5)

    def start_pos(self):
        self.teleport(0,random.randint(-int(self.half_height*0.75),int(self.half_height*0.75)))
        self.setheading(random.choice(ANGLE))

    def move(self):
        self.fd(10)

    def reflection(self):
        self.setheading(360-self.heading())
        self.fd(10)

    def paddle_ref(self):
        if self.heading() == 0 :
            self.setheading(random.choice([30,150]))
        elif self.heading() == 180 :
            self.setheading(random.choice([330,210]))
        self.setheading(540-self.heading())
        self.fd(10)
        
