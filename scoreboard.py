from turtle import Turtle


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_player_score = 0
		self.r_player_score = 0
		self.goto(-180, 290)
		self.write(self.l_player_score, align="center", font=("Courier", 18, "normal"))
		self.goto((180, 290))
		self.write(self.r_player_score, align="center", font=("Courier", 18, "normal"))

	def update_score(self):
		self.clear()
		self.goto(-180, 290)
		self.write(self.l_player_score, align="center", font=("Courier", 18, "normal"))
		self.goto((180, 290))
		self.write(self.r_player_score, align="center", font=("Courier", 18, "normal"))

	def l_point(self):
		self.l_player_score += 1

	def r_point(self):
		self.r_player_score += 1
