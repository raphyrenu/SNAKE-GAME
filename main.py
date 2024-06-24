import time
from turtle import Turtle, Screen

from score import Score
from food import Food
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("dodgerBlue")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True;

while game:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase() 

        score.scores()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or \
            snake.turtles[0].ycor() < -280:
        food.refresh()
        score.reset_score()
        snake.reset_snake()

    for part in snake.turtles[1:]:

        if snake.turtles[0].distance(part) < 10:
            food.refresh();
            score.reset_score();
            snake.reset_snake()

screen.exitonclick()
