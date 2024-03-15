# import the modules we need:
from turtle import Turtle

# set the variables:
STEP = 50
UP = 90
DOWN = 270

# set the class:


class Paddle(Turtle):
	def __init__(self, what_side):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.speed("fastest")
		self.penup()
		self.goto(what_side)
		self.move_up()
		self.move_down()

	def move_up(self):
		if self.ycor() < 230:
			self.setheading(UP)
			self.forward(STEP)

	def move_down(self):
		if self.ycor() > -230:
			self.setheading(DOWN)
			self.forward(STEP)