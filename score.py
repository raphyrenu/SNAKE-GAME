from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("black")

        self.goto(0, 265)
        self.write(f"score: {self.score} High score: {self.high_score}", align='center', font=('arial', 24, 'normal'))



    def scores(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score} High score: {self.high_score}", align='center', font=('arial', 24, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = -1
        self.scores()




