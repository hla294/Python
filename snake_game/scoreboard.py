from turtle import Turtle

# Global values that stay consistent
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # score 0 initializing
        with open("data.txt") as data:  # loading the highest score from the previous game
            self.high_score = int(data.read())
        self.color("white")  # color of the score board
        self.penup()  # avoiding drawing a line to the position of the score
        self.goto(0, 270)  # score board location
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)  # writing a score board

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:  # updating the highest score in the data.txt file
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
