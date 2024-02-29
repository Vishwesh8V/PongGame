from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.shape("circle")
        self.turtlesize()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def collision(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
