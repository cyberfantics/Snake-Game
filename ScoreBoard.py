from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"
SCORE_SPEED = 5


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.h_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def reset(self):
        if self.score > self.h_score:
            self.h_score = self.score
            with open("highscore.txt", "w") as data:
                data.write(f"{self.h_score}")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.h_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += SCORE_SPEED
        self.update()
