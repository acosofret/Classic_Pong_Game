# import the modules we need:
from turtle import Turtle

# set the variables:


# set the class:


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.y_step = 1
		self.x_step = 1.5
		self.move_speed = 0.015

	def move(self):
		new_x = self.xcor() + self.x_step
		new_y = self.ycor() + self.y_step
		self.goto(new_x, new_y)

	def wall_bounce(self):
		self.y_step *= -1

	def paddle_bounce(self):
		self.x_step *= -1

	def reset(self):
		self.move_speed = 0.015
		self.goto(0, 0)
		self.x_step *= -1
		self.move()
