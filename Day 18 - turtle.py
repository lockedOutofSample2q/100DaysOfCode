import turtle as Turtleh
import random   

rgb_colors=[[31, 31, 31], [155, 219, 252], [110, 186, 162], [217, 219, 171], [124, 99, 37], [38, 110, 158], [84, 172, 233], [220, 210, 119], [171, 208, 180], [207, 173, 86]]

newTurtle = Turtleh.Turtle()

newTurtle.shape('turtle')
newTurtle.color("black")
Turtleh.colormode(255)   

def draw_n_sided(j):
    for i in range(j):
        newTurtle.forward(100)
        newTurtle.right(360/j)
        
available_colors = ["purple", "black", "pink", "green", "yellow", "magenta", "red"]
direction = [0,90,180,270]

newTurtle.pensize(5)

def draw_random_walk():
    for i in range(922):
        newTurtle.forward(30)
        newTurtle.right(random.choice(direction))
        newTurtle.pencolor(random.choice(available_colors))
    

def draw_spirograph():
    for i in range(0,360,5):
        newTurtle.pencolor(random.choice(available_colors))
        newTurtle.setheading(i)
        newTurtle.circle(100)

def draw_dot_pattern():
    newTurtle.penup() 
    newTurtle.setheading(225)
    newTurtle.forward(300)
    for j in range(100):
        if j%10==0:
            newTurtle.setheading(90)
            newTurtle.forward(30)
            newTurtle.setheading(180)
            newTurtle.forward(300)
            newTurtle.setheading(0)  

        newTurtle.pendown()
        newTurtle.dot(20,random.choice(rgb_colors))
        newTurtle.penup() 
        newTurtle.forward(30)

newTurtle.speed(15)
draw_dot_pattern()
screen = Turtleh.Screen()
    
screen.exitonclick()


