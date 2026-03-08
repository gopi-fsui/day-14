from turtle import Turtle

class BackGround(Turtle):
    def __init__(self,x:int,y:int,bg_color:str="white",center_dash_line:bool = False):
        super().__init__()
        self.half_x_area = int(x / 2)
        self.half_y_area = int(y / 2)
        self.bg_color = bg_color
        self.dash_line = center_dash_line
        self.hideturtle()
        self.penup()
        self.draw_bg(self.bg_color,self.dash_line)


    def draw_bg(self,color, dash_line ):
        """Draw a self using specified color, value should be str"""
        self.color(color)
        self.goto(self.half_x_area, self.half_y_area)
        self.begin_fill()
        for opt in [-1, 1]:
            self.goto(opt * self.half_x_area, opt * (-self.half_y_area))
            self.goto(opt * self.half_x_area, opt * self.half_y_area)
        self.end_fill()

        if dash_line:
            self.draw_center_dashline()


    def draw_center_dashline(self):
        self.goto(0,self.half_y_area)
        self.color("black")
        self.width(4)
        self.setheading(270)
        for x in range(int((self.half_y_area*2)/25)):
            self.pendown()
            self.fd(12)
            self.penup()
            self.fd(14)
