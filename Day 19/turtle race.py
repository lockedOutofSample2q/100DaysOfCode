from turtle import *
import random

colors=["red","green","cyan","blue","pink","violet"]
turtle_list = []
start_race = False
y_pos = -150
for i in range(6):
       
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colors[i])
    newTurtle.setposition(x=-330,y=y_pos)
    turtle_list.append(newTurtle)
    y_pos +=60



screen = Screen()
screen.setup(width=700,height=500)
user_bet=screen.textinput(title= "",prompt="Make your bets, on who you think will win : ")

if user_bet :
    start_race = True

while start_race:
    for turtle in turtle_list:
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)
        if turtle.position()[0] >= 330:
            winning_turtle = turtle.color()[0]
            if winning_turtle == user_bet:
                print("Congrats!")
            print(f"{winning_turtle} turtle won")
            start_race=False
    


screen.exitonclick()
