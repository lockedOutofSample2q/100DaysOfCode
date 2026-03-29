import time
from Snake import Snake
from turtle import Screen
from food import Food
from score import Score


def gameover():
    snake_instance.hide()
    food_instance.hide() 
    game_screen.update()
    score_instance.printFinalScore()


game_screen = Screen()
game_screen.setup(width = 600, height = 600)
game_screen.bgcolor("black")
game_screen.title("Nokia Snake")


game_screen.tracer(0)

snake_instance = Snake()
food_instance = Food()
score_instance = Score()



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
    if snake_instance.head.distance(food_instance) < 15:
        score_instance.increase_score()
        food_instance.spawn()
        snake_instance.get_food_get_long()
    score_instance.display_score()
    if -280 < snake_instance.head.xcor() < 280 and -280 < snake_instance.head.ycor() < 260:
        pass
    else :
        gameover()
        game_is_on=False
       
    for body_segment in snake_instance.snake_body[3:]:
        if snake_instance.head.distance(body_segment)<10:
            game_is_on = False
            gameover()

              
        

    

    
    





game_screen.exitonclick()
