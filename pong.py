from turtle import Turtle

HEIGHT = 5
WIDTH = 1
MOVE_DISTANCE = 20


class Pong(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.penup()
        self.goto(positions)
        self.move_up = False
        self.move_down = False

    def up(self):
        self.move_up = True
        if self.ycor() < 245:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        self.move_down = True
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def stop_move(self):
        self.move_up = False
        self.move_down = False

