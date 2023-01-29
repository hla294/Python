from turtle import Turtle

"""
Global values of attributes of directions of the snake
"""
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """
        Initializing the snake
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Snake being longer
        :return:
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segmen to the snake getting longer.
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Movign snake
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Moves Snake
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        snake heading up
        :return:
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        """
        snake heading down
        :return:
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """
        snake heading right
        :return:
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        """
        snake heading left
        :return:
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
