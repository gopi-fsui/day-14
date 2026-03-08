from turtle import Turtle
import random

ANGLE = [0,30,150,180,210,330]

class Ball(Turtle):
    def __init__(self,height:int):
        super().__init__("circle")
        self.half_height = int(height/2)
        self.color("black")
        self.penup()

    def start_pos(self):
        self.teleport(0,random.randint(-int(self.half_height*0.75),int(self.half_height*0.75)))
        self.setheading(random.choice(ANGLE))

    def move(self):
        self.fd(5)
        
    def reflection(self):
        self.setheading(360-self.heading())
