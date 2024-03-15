import time
from turtle import Screen
from paddle import Paddle
from walls import Walls
from ball import Ball
from scoreboard import ScoreBoard

walls = Walls()
game_on = True
PADDLE_POSITIONS = [(350, 0), (-350, 0)]
right = PADDLE_POSITIONS[0]
left = PADDLE_POSITIONS[1]
speed = 0.015


# Create the screen
screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.tracer(0)

walls.draw_wall()

# Make 1st paddle and make it move
paddle_r = Paddle(right)
screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

# Create another paddle
paddle_l = Paddle(left)
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

# Create the ball
ball = Ball()

# Keep score
scoreboard = ScoreBoard()

while game_on:
	time.sleep(ball.move_speed)
	screen.update()

	# and make it move (ball)
	ball.move()

	# Detect collision with wall and bounce
	if ball.ycor() > 250 or ball.ycor() < -250:
		ball.wall_bounce()

	# Detect collision with RIGHT paddle and bounce
	if ball.xcor() > paddle_r.xcor() - 30 and ball.distance(paddle_r) <= 52:
		if ball.move_speed > 0.002:
			ball.move_speed -= 0.001
		ball.paddle_bounce()
		print(ball.move_speed)

	# Detect collision with LEFT paddle and bounce
	if ball.xcor() < paddle_l.xcor() + 30 and ball.distance(paddle_l) <= 52:
		if ball.move_speed > 0.002:
			ball.move_speed -= 0.001
		ball.paddle_bounce()
		print(ball.move_speed)

	# Detect when r_paddle misses
	if ball.xcor() > 500 and ball.distance(paddle_r) > 52:
		scoreboard.l_point()
		scoreboard.update_score()
		ball.reset()
	# Detect when l_paddle misses
	if ball.xcor() < -500 and ball.distance(paddle_l) > 52:
		scoreboard.r_point()
		scoreboard.update_score()
		ball.reset()



screen.exitonclick()
