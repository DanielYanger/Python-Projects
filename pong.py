import turtle
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

left_score = 0
right_score = 0

#left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("#1cfc03")
paddle_left.penup()
paddle_left.setpos(-350, 0)

#Right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color("#1cfc03")
paddle_right.penup()
paddle_right.setpos(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.setpos(0, 0)
ball.xvel = random.randrange(-10, 10)*.075
ball.yvel = random.randrange(-10, 10)*.075

#titles
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Player A: 0 Player B: 0",
          align='center',
          font=("Arial", 24, "normal"))


#Functions
def paddle_right_up():
    y = paddle_right.ycor()
    if y < 240:
        y += 30
        paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    if y > -240:
        y -= 30
        paddle_right.sety(y)


def paddle_left_up():
    y = paddle_left.ycor()
    if y < 240:
        y += 30
        paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    if y > -240:
        y -= 30
        paddle_left.sety(y)


#Bindings
wn.listen()
wn._onkeypress(paddle_left_down, "s")
wn._onkeypress(paddle_left_up, "w")
wn._onkeypress(paddle_right_down, "Down")
wn._onkeypress(paddle_right_up, "Up")

#Main Game
while True:
    wn.update()

    #Update Ball Postition
    ball.setpos(ball.xcor() + ball.xvel, ball.ycor() + ball.yvel)

    #Check for top and bottom borders
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.yvel *= -1

    #Scoring
    if ball.xcor() > 350:
        left_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(left_score, right_score),
                  align="center",
                  font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.xvel = ball.xvel / abs(ball.xvel) * -.5
        ball.yvel = ball.yvel / abs(ball.yvel) * .5

    elif ball.xcor() < -350:
        right_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(left_score, right_score),
                  align="center",
                  font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.xvel = ball.xvel / abs(ball.xvel) * -.5
        ball.yvel = ball.yvel / abs(ball.yvel) * .5
    #Hitting the paddle
    if ball.xcor() > 330 and ball.ycor(
    ) < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50:
        ball.xvel *= -random.randrange(1000, 1300) * .001
        ball.yvel *= -random.randrange(1000, 1300) * .001

    if ball.xcor() < -330 and ball.ycor(
    ) < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
        ball.xvel *= -random.randrange(1000, 1300) * .001
        ball.yvel *= -random.randrange(1000, 1300) * .001
