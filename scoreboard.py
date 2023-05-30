from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 70, 'normal')


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f'{self.score}', True, align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.undo()
        self.write(f'{self.score}', True, align=ALIGN, font=FONT)

