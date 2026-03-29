from turtle import Turtle
import random

color = ["pink","purple","red","yellow","white"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(color)) 
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.spawn()
        
    
    def spawn(self):
        ranX = random.randint(-280,280)
        ranY = random.randint(-280,260)
        self.goto(ranX, ranY)
    def hide(self):
        self.hideturtle()
    
          