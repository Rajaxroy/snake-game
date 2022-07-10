from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            new_high_score = file.read()

        self.high_score = int(new_high_score)
        self.color("white")
        self.penup()
        self.goto(0, 265)

        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:

                data.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))
