from turtle import Screen
from time import sleep
from Snake import Snake
from Food import Food
from Scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Shack Game')
screen.tracer(0)

snake = Snake()
food = Food()
ScoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.onkey(snake.down, 's')
screen.onkey(snake.up, 'w')

counter = 1
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.check_distance(food):
        food.refresh_food_place()
        snake.extend_body()
        ScoreBoard.create_score()

    if snake.border_check() is True:
        ScoreBoard.reset_score()
        snake.reset()

    if snake.body_eat_check():
        ScoreBoard.reset_score()
        snake.reset()




screen.exitonclick()
