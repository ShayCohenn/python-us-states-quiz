from turtle import Turtle

FONT = ("Courier", 8, "normal")

class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.pensize(1)
    
    def update_text(self, x, y, state):
        self.clear()
        self.goto(x, y)
        self.write(state, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("You Won!, press 'R' to restart", align='center', font=("Courier",26, "normal"))