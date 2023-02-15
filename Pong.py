#Pong
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball_a = turtle.Turtle()
ball_a.speed(0)
ball_a.shape("square")
ball_a.color("white")
ball_a.shapesize(stretch_wid=1, stretch_len=1)
ball_a.penup()
ball_a.goto(0, 0)
ball_a.dx = 3
ball_a.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#score
score_a = 0
score_b = 0

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball_a.setx(ball_a.xcor() + ball_a.dx)
    ball_a.sety(ball_a.ycor() + ball_a.dy)

    # Boundaries
    if ball_a.ycor() > 290:
        ball_a.sety(290)
        ball_a.dy *= -1

    if ball_a.ycor() < -290:
        ball_a.sety(-290)
        ball_a.dy *= -1

    if ball_a.xcor() > 390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball_a.xcor() < -390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball_a.xcor() > 330 and ball_a.xcor() < 350) and (ball_a.ycor() < paddle_b.ycor() + 40 and ball_a.ycor() > paddle_b.ycor() - 50):
        ball_a.dx *= -1


    if (ball_a.xcor() < -330 and ball_a.xcor() > -350) and (ball_a.ycor() < paddle_a.ycor() + 40 and ball_a.ycor() > paddle_a.ycor() - 50):
        ball_a.dx *= -1





