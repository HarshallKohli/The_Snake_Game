from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

#  importing properties from the Snake class from snake.py file
snake = Snake()
#  importing properties from the Food class from food.py file
food = Food()
#  importing properties from the Scoreboard class from scoreboard.py file
scoreboard = Scoreboard()

#  allowing movement of the snake using arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # our snake is moving quite faster now with a small input value.
    snake.move()   # calling the move() function from snake.py file

# TODO 4: Detecting collision with food and allowing a random position for the next food to be placed
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()  # updating score everytime snake reaches food

#  TODO 6: Detecting collision with wall, stopping the game by printing "Game Over!"
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


#  TODO 7: Detecting collision with its growing tail, stopping the game by printing "Game Over!"
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
