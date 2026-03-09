from turtle import Turtle

class  ScoreCard(Turtle):
    def __init__(self,width,height,name:str,color:str="white"):
        super().__init__()
        self.score = 0
        self.width = width
        self.height = height
        self.name = name
        self.hideturtle()
        self.color(color)
        self.update_score()

    def update_score(self):
        self.clear()
        self.teleport(int(self.width), int(self.height) + 70)
        self.write(F"{self.name}", align="center", font=("arial", 20, "bold"))
        self.teleport(int(self.width), int(self.height) + 30)
        self.write(F"{self.score}", align="center", font=("arial", 30, "bold"))

