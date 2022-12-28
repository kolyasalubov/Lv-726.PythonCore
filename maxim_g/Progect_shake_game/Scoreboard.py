from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.hideturtle()
        self.basic_score = 0
        self.high_score = self.get_score_data()
        self.create_score()

    def create_score(self):
        self.clear()
        self.write(f'Score: {self.basic_score} High score: {self.high_score}', False, align='center',
                   font=('courier', 24, 'normal'))
        self.basic_score += 1

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f'Game over!', False, align='center', font=('courier', 24, 'normal'))

    def reset_score(self):
        if self.basic_score > self.high_score:
            self.high_score = (self.basic_score - 1)
            self.set_score_data()
        self.basic_score = 0
        self.create_score()

    def get_score_data(self):
        with open(file="data.txt", mode='r') as file:
            score_from_file = int(file.read())
        return score_from_file

    def set_score_data(self):
        with open(file="data.txt", mode='w') as file:
            file.write(str(self.high_score))
