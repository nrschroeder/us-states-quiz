from turtle import Turtle
class StateName(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, user_answer):
        self.color("black")
        self.write(arg=user_answer, align="center", font=("Arial", 6, "normal"))

    def place_state(self, x, y):
        self.goto(x, y)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="CONGRATS! You named all 50", align="center", font=("Comic Sans", 30, "bold"))