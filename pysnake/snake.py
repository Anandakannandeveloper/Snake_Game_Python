import turtle
import time
import random

delay=0.1  


#Score
score=0
hscore=0

#  window screen for game

window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600 ,height=600)
window.tracer(0)   #turns off the screen updates


# creation of the snake head 
snhead = turtle.Turtle()
snhead.speed(0)
snhead.shape("square")
snhead.color("yellow")
snhead.penup()     #so that no lines are drawn
snhead.goto(0,0)   #when head starts it must be in the centre of the screen
snhead.direction="stop"

# snake food
snfood = turtle.Turtle()
snfood.speed(0)
snfood.shape("circle")
snfood.color("red")
snfood.penup()     #so that no lines are drawn
snfood.goto(0,100)   #when head starts it must be in the centre of the screen



#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0",align="center", font=("Courier",24, "normal"))        #write function helps to display text in graphics window


segments=[]


#functions

def go_up():
    if snhead.direction != "down":   #preventing from going in reverse
        snhead.direction="up"

def go_down():
    if snhead.direction != "up":
        snhead.direction="down"

def go_left():
    if snhead.direction != "right":
        snhead.direction="left"

def go_right():
    if snhead.direction != "left":
        snhead.direction="right"


def move():
    if snhead.direction=="up":
        y=snhead.ycor()
        snhead.sety(y+20)
    if snhead.direction=="down":
        y=snhead.ycor()
        snhead.sety(y-20)
    if snhead.direction=="left":
        x=snhead.xcor()
        snhead.setx(x-20)
    if snhead.direction=="right":
        x=snhead.xcor()
        snhead.setx(x+20)


#keyboard bindings
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"Down")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"Left")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"Right")
window.onkeypress(go_right,"d")



#main game loop
while True:
    window.update()

    # check for a collision with border
    if snhead.xcor()>290 or snhead.xcor()<-290 or snhead.ycor()>290 or snhead.ycor()<-290:
        time.sleep(1)
        snhead.goto(0,0)
        snhead.direction="stop"

        #hide the segments
        for s in segments:
            s.goto(1000,1000)     # moving to top right off the screen 

        #clear the segments list
        segments.clear()
 
        #reset the score
        score=0

        #reset the delay so snake moves slowly from first
        delay=0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,hscore),align="center", font=("Courier",24, "normal"))        



    #check for collision with food
    if snhead.distance(snfood)<20:
        #move food to random spot as snake colloids the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        snfood.goto(x,y)


        # adding segment
        nsegment=turtle.Turtle()
        nsegment.speed(0)
        nsegment.shape("square")
        nsegment.color("green")
        nsegment.penup()
        segments.append(nsegment)


        #shorten delay   after eating and becoming longer so speed of snake increases
        delay-=0.001

        #Increase the score
        score+=10

        if score>hscore:
            hscore=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,hscore),align="center", font=("Courier",24, "normal"))        


    #move the end segments first in reverse order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    #move segment 0 to where the head is
    if len(segments)>0:
        x=snhead.xcor()
        y=snhead.ycor()
        segments[0].goto(x,y)


    move()


    #check for the head collision with the body segments
    for s in segments:
        if s.distance(snhead) < 20:   #this means that they are overlapping
            time.sleep(1)
            snhead.goto(0,0)
            snhead.direction = "stop"

            #hide the segments
            for s in segments:
                s.goto(1000,1000)     # moving to top right off the screen 

            #clear the segments list
            segments.clear()

            #reset the score
            score=0

            #reset the delay so snake moves slowly from first
            delay=0.1

            #update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,hscore),align="center", font=("Courier",24, "normal"))        



    time.sleep(delay)  #so that it is not too fast
    
window.mainloop()   #helps to show and appear window screen



#no need to install turtle as it comes with py