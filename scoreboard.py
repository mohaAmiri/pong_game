from turtle import Turtle


class Scoreboard(Turtle):
    """ Print Scores and messages on the screen """

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def welcome(self):
        """ print instruction at the beginning """
        self.welcome_message = Turtle()
        self.welcome_message.penup()
        self.welcome_message.color("white")
        self.welcome_message.goto(0, 0)
        self.welcome_message.hideturtle()
        self.welcome_message.write("Press Enter to start!", align="center", font=("Courier", 24, "normal"))
        self.welcome_message.goto(0, -50)
        self.welcome_message.write("Click on screen to quit!", align="center", font=("Courier", 18, "normal"))

    def pause_game_message(self):
        """ print stop game message """
        self.stop_message = Turtle()
        self.stop_message.penup()
        self.stop_message.color("white")
        self.stop_message.goto(0, -250)
        self.stop_message.hideturtle()
        self.stop_message.write("Press ESC to stop!", align="center", font=("Courier", 18, "normal"))
        self.stop_message.goto(0, -280)
        self.stop_message.write("Press Space to restart!", align="center", font=("Courier", 12, "normal"))
