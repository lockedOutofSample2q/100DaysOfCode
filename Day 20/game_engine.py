from turtle import Turtle
PLACE = [0,-20,-40]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():


    def __init__(self):
        self.snake_body = []
        self.create_snake_body()
        self.head = self.snake_body[0]

    def create_snake_body(self):
        for i in range(3):
            newTurtle = Turtle(shape="square")
            newTurtle.color("white")
            newTurtle.penup()
            newTurtle.setposition(PLACE[i],0)
            self.snake_body.append(newTurtle)

    def move(self):
        
        for segment_number in range(len(self.snake_body)-1,0,-1):
            prev_segment_x = self.snake_body[segment_number-1].xcor()
            prev_segment_y = self.snake_body[segment_number-1].ycor()
            self.snake_body[segment_number].setposition(prev_segment_x,prev_segment_y)
        self.head.forward(STEP)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
