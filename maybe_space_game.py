import turtle
import random

wind=turtle.Screen()
wind.screensize(500,500)
wind.bgcolor("#000")


player = turtle.Turtle()
player.speed(0)
player.color("green")

player.shape("square")
player.shapesize(2,1,0)

player.penup()


player.goto(0,-250)

def moveR():
    x=player.xcor()
    x+=20
    player.setx(x)

def moveL():
    x=player.xcor()
    x-=20
    player.setx(x)

wind.listen()
wind.onkeypress(moveR,"Right")
wind.onkeypress(moveL,"Left")

shots = turtle.Turtle()
shots.hideturtle()
shots.goto(0,-230)
shots.showturtle()
shots.color("blue")
shots.shape("square")
shots.shapesize(0.5,0.3,0)
shots.penup()
shots.speed(0)

shots.dy = 4


enimy = turtle.Turtle()
enimy.hideturtle()
enimy.goto(0,270)
enimy.showturtle()
enimy.speed(0)
enimy.color("red")
enimy.shape("square")
enimy.shapesize(2,2,0)
enimy.penup()

enimyshots=turtle.Turtle()
enimyshots.hideturtle()
enimyshots.goto(0,240)
enimyshots.showturtle()
enimyshots.color("red")
enimyshots.shape("square")
enimyshots.shapesize(0.5,0.3,0)
enimyshots.penup()
enimyshots.speed(0)

enimyshots.dy = 2

gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("#fff")
gameover.penup()
gameover.hideturtle()
gameover.goto(0,0)

# gameover.write("Game Over")

score = turtle.Turtle()
score.speed(0)
score.color("#fff")
score.penup()
score.hideturtle()
score.goto(0,-100)


s=0


while True:
    
    wind.update()
    r = random.randint(-2,2)
    if(player.xcor()>=300):
        player.setx(300)

    if(player.xcor()<=-300):
        player.setx(-300)
    if(shots.ycor()==-250):
        shots.setx(player.xcor())
    if(shots.ycor() >=300):
        shots.hideturtle()
        shots.goto(player.xcor(),player.ycor() + 20)
        shots.showturtle()

    if( (shots.ycor()==enimy.ycor()-20) and ((shots.xcor()==enimy.xcor()) or (shots.xcor()==enimy.xcor()+20) or (shots.xcor()==enimy.xcor() - 20))):
        enimy.hideturtle()
        enimy.goto(r*100,270)
        enimy.showturtle()
        s+=1
        enimyshots.dy +=2

    
    
    
    
    if(enimyshots.ycor()==-250):
        enimyshots.setx(enimy.xcor())
    if(enimyshots.ycor() <=-300):
        enimyshots.hideturtle()
        enimyshots.goto(enimy.xcor(),enimy.ycor() + 30)
        enimyshots.showturtle()
    if( ( enimyshots.ycor() == player.ycor()+20 ) and ( player.xcor() == enimyshots.xcor() ) ):
    
        player.hideturtle()
        shots.hideturtle()
        enimy.hideturtle()
        enimyshots.hideturtle()
        
        gameover.write("Game Over" ,False,"center",['',20,''])
        score.write(f"enimies you killed : ( {s} )" ,False,"center",['',10,''])
    else:
        shots.sety(shots.ycor() + shots.dy)
        enimyshots.sety(enimyshots.ycor() - enimyshots.dy)
        
