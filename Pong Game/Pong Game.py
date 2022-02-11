import turtle
import winsound

# Screen
win = turtle.Screen()
win.title("Pong by @MILK")
win.bgcolor("black")
win.setup(width = 900, height = 700)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# Function
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

# Keybind
win.listen()
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_a_up, "w")

# Main Game Loop
while True:
    win.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1    
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)     

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  

    if ball.xcor() > 440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # Collisions
    if (ball.xcor() > 390 and ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(390)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  

    if (ball.xcor() < -390 and ball.xcor() > -400) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-390)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  

