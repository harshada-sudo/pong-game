import turtle
import winsound

#create window
wn = turtle.Screen()
wn.title("ping pong game")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0) #stops window from updating

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle() #turtle object
paddle_a.speed(0) #speed of animation maximum speed
paddle_a.shape("square") #default shape = 20x20 px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #change size of turtle
paddle_a.penup() 
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle() #turtle object
paddle_b.speed(0) #speed of animation maximum speed
paddle_b.shape("square") #default shape = 20x20 px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle() #turtle object
ball.speed(0) #speed of animation maximum speed
ball.shape("circle") #default shape = 20x20 px
ball.color("white")
ball.penup() 
ball.goto(0,0)
ball.dx = 0.4
ball.dy = -0.4

#pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A :  0   Player B :  0",align="center",font=('times new roman',20,'normal'))

#define functions
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#keyboard binding
turtle.listen() #listen keyboard input 
turtle.onkeypress(paddle_a_up,"w")
turtle.onkeypress(paddle_a_down,"s")
turtle.onkeypress(paddle_b_up,"Up")
turtle.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
    wn.update() #everytime loop runs it updates the screen

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction 2*-1 = -2
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    #bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverse direction 2*-1 = -2    
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
       
    #left border
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A :  {}   Player B :  {}".format(score_a,score_b),align="center",font=('times new roman',20,'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A :  {}   Player B :  {}".format(score_a,score_b),align="center",font=('times new roman',20,'normal'))
    
    #paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        
