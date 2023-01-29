from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game by Samuel Lee")
screen.tracer(0) # automatic screen updates are off, no animation in the beginning of the screen

r_paddle = Paddle((350, 0))  # paddle for the right user
l_paddle = Paddle((-350, 0)) # paddle for the left user
# top_paddle = Paddle((100,100))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # onkey(function, key)
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()