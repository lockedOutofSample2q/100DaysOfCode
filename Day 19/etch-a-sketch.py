import turtle
from turtle import *


newturtle = turtle.Turtle()

def move_up():
    newturtle.forward(10)

def move_down():
    newturtle.backward(10)

def move_right():
    headingdir = newturtle.heading() - 10
    newturtle.setheading(headingdir)

def move_left():
    headingdir = newturtle.heading() + 10
    newturtle.setheading(headingdir)
    

def clearscreens():
    newturtle.reset()

screen = turtle.Screen()
listen()
onkey(key='w',fun=move_up)
onkey(key='s',fun=move_down)
onkey(key='a',fun=move_left)
onkey(key='d',fun=move_right)
onkey(key='c',fun=clearscreens)



screen.exitonclick()
