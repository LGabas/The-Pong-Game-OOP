from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_direction = 1
        self.y_direction = 1
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + (MOVE_DISTANCE * self.x_direction)
        y_pos = self.ycor() + (MOVE_DISTANCE * self.y_direction)
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
        self.bounce_y()





