from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game by Samuel Lee")
screen.tracer(0) # automatic screen updates are off, no animation in the beginning of the screen

r_paddle = Paddle((350, 0))  # paddle for the right user
l_paddle = Paddle((-350, 0)) # paddle for the left user
# top_paddle = Paddle((100,100))
ball = Ball()

screen.listen() # In order to use keyboard buttons to interact with the program
screen.onkey(r_paddle.go_up, "Up")  # onkey(function, key)
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # slow down the ball speed
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    # Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # Debug: print("Made Contact")
        ball.bounce_x()

screen.exitonclick()