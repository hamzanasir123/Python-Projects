
# simple Pong in python 

import turtle

win = turtle.Screen()
win.title("Pong Game By Hamza Nasir")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

# score 
score1 = 0
score2 = 0


# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))





# functinality

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# keyword Binding
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")

win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

# Game Loop

while True:
    win.update()


    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
    pen.clear()
    pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # Paddle and Ball Collisions
    if (ball.dx > 0) and (350 < ball.xcor() < 360) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.dx < 0) and (-350 > ball.xcor() > -360) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Paddle and Border Collisions
    if paddle1.ycor() > 250:
        paddle1.sety(250)
    elif paddle1.ycor() < -250:
        paddle1.sety(-250)


    if paddle2.ycor() > 250:
        paddle2.sety(250)
    elif paddle2.ycor() < -250:
        paddle2.sety(-250)
    