from turtle import Turtle
import random

# TODO 3: Creating the snake food


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")             # the food is in the shape of a circle
        self.penup()                     # to avoid drawing on the screen
        self.shapesize(0.5, 0.5)         # len and wid of circle
        self.color("red")
        self.speed("fastest")
        self.refresh()

#  allowing a random position for the food
    def refresh(self):
        random_x = random.randint(-280, 280)  # setting x co-ordinate in screen
        random_y = random.randint(-280, 280)  # setting y co-ordinate in screen
        self.goto(random_x, random_y)           # where food can be anywhere in (x,y) ordinates



