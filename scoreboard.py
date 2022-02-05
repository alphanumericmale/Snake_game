from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open('high_score.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.setposition(0, 255)
        self.hideturtle()
        self.score_increase()

    def score_increase(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as data:
                data.write(str(self.score))
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align='center', font=("Arial", 20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=("Arial", 20, "normal"))
