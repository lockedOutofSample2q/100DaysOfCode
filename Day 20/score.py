FONT = ('Cabin', 15, 'normal')
ALIGNMENT = 'center'
BIGFONT = ('Courier', 18, 'normal')



from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.display_score()
        

    def display_score(self):  
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def printFinalScore(self):
        self.clear()
        self.goto(0,0)
        self.write(f"     GAME OVER!\nYour final score is: {self.score}", align=ALIGNMENT, font=BIGFONT)

    
