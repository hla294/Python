from turtle import Turtle

# Global values that stay consistent
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # score 0 initializing
        self.color("white")  # color of the score board
        self.penup()  # avoiding drawing a line to the position of the score
        self.goto(0, 270)  # score board location
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # writing a score board

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear() # delete the previous score to avoid a new score being written over the previous score
        self.update_scoreboard()
