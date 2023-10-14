import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

""" Screen Setup """
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

""" paddles, ball and scoreboard instances """
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.welcome()

""" control keyboard inputs """
screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

game_is_on = True


def restart_game():
    scoreboard.l_score = 0
    scoreboard.r_score = 0
    scoreboard.update_scoreboard()
    global game_is_on
    game_is_on = True
    ball.reset_position()
    r_paddle.goto(350, 0)
    l_paddle.goto(-350, 0)


def pause_game():
    global game_is_on
    game_is_on = False
    scoreboard.welcome()
    scoreboard.stop_message.clear()


def start_game():
    global game_is_on
    game_is_on = True
    scoreboard.welcome_message.clear()
    scoreboard.pause_game_message()
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        """ Detect collision with wall """
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        """detect collision with paddle"""
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        """ detect when r_paddle misses"""
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        """ detect when l_paddle misses """
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()


""" start, pause and restart buttons """
screen.onkey(start_game, "Return")
screen.onkey(restart_game, "space")
screen.onkey(pause_game, "Escape")
screen.exitonclick()
