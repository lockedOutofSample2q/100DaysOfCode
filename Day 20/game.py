import time
from Snake import Snake
from turtle import Turtle, Screen



game_screen = Screen()
game_screen.setup(width = 600, height = 600)
game_screen.bgcolor("black")
game_screen.title("Nokia Snake")

snake_instance = Snake()

game_screen.tracer(0)

game_is_on = True

game_screen.listen()

game_screen.onkey(key='w', fun= snake_instance.move_up )
game_screen.onkey(key='s', fun= snake_instance.move_down)
game_screen.onkey(key='a', fun= snake_instance.move_left)
game_screen.onkey(key='d', fun= snake_instance.move_right)

while game_is_on:
    snake_instance.move()
    game_screen.update()
    time.sleep(0.09)
    
    





game_screen.exitonclick()
