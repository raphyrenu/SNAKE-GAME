import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add(position)

    def add(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.shapesize(0.4, 0.4)
        snake.penup()
        snake.goto(position)
        self.turtles.append(snake)

    def increase(self):
        self.add(self.turtles[-1].position())

    def reset_snake(self):
        for tim in self.turtles:
            tim.goto(10000, 10000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]


    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            self.head.setheading(RIGHT)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(LEFT)
