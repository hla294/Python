from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """
        Initializing the attributes of the blue food
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.refresh()

    def refresh(self):
        """
        the random location of the food after being eaten
        :return->None:
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

