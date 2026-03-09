from turtle import Turtle
MOVE_STEP = 25
class Paddle:
    def __init__(self,start_pos_x,height):
        self.half_height = height/2
        self.start_pos_x = start_pos_x
        self.paddles_boxes = []
        self.add_paddle_boxes()
        self.center_paddle = self.paddles_boxes[2]
        self.set_paddle()

    def add_paddle_boxes(self):
        for y in [-20, -10, 0, 10, 20]:
            new_paddle = Turtle("square")
            new_paddle.color("Red")
            new_paddle.shapesize(0.5)
            new_paddle.penup()
            new_paddle.goto(0, y)
            self.paddles_boxes.append(new_paddle)


    def set_paddle(self):
        for item in self.paddles_boxes:
            item.goto(self.start_pos_x, item.ycor())
            item.setheading(90)

    def move_up(self):
        # print("")
        if  self.center_paddle.ycor() < self.half_height - MOVE_STEP:
            for item in self.paddles_boxes:
                item.fd(MOVE_STEP)

    def move_down(self):
        if  self.center_paddle.ycor() > -(self.half_height - MOVE_STEP):
            for item in self.paddles_boxes:
                item.bk(MOVE_STEP)
                
