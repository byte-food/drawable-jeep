from turtle import write, fillcolor, circle, pencolor, hideturtle, penup, pendown, begin_fill, getscreen, title, bgcolor, end_fill, goto, speed, pensize, dot
from random import randint
#initiate screen and turtle object
screen = getscreen()
title("Happy Birthday Omar!")
bgcolor("#2a2a35")
hideturtle()

def drawRoad(s=5):
    speed(s)
    penup()
    goto(-700, -100)
    pendown()
    begin_fill()
    goto(700, -100)
    goto(700, -400)
    goto(-700, -400)
    goto(-700, -100)
    end_fill()
    penup()
    goto(0,0)
    pendown()

def drawStars(s=9):
    speed(s)
    penup()
    pencolor("white")
    for i in range(randint(100, 200)):
        goto(randint(-700, 700), randint(200, 300))
        dot(size=4)
    pencolor("black")
    goto(0, 0)
    pendown()
def drawWheels(s=2):
    speed(s)
    #wheel 1
    penup()
    goto(-50, -100)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    #reset
    pencolor("black")
    fillcolor("black")
    
    #wheel 2
    penup()
    goto(50, -100)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    #final reset
    pencolor("black")
    fillcolor("black")
    penup()
    goto(0,0)
    pendown()

def drawBody(s=1):
    speed(s)
    penup()
    pensize(10)
    goto(-70, -85)
    pendown()
    goto(70, -85)
    pensize(1)
    fillcolor("#967117")
    begin_fill()
    goto(70, -15)
    goto(-30, -15)
    goto(-40, -45)
    goto(-70, -45)
    goto(-70, -65)
    pensize(15)
    goto(-70, -85)
    end_fill()
    pensize(1)
    fillcolor("black")

def drawBackWheel(s=1):
    penup()
    goto(75, -65)
    speed(s)
    pendown()
    pensize(15)
    goto(75, -45)
    penup()
    goto(0, 0)
    pensize(1)
    
def drawWindow(s=1):
    #window 1
    speed(s)
    fillcolor("#357EC7")
    pencolor("black")
    begin_fill()
    goto(-30, -20)
    goto(-40, -45)
    goto(-5, -45)
    goto(-5, -20)
    goto(-30, -20)
    end_fill()
    penup()
    
    #window 2
    goto(0, -20)
    pendown()
    begin_fill()
    goto(30, -20)
    goto(30, -45)
    goto(0, -45)
    goto(0, -20)
    end_fill()
    penup()

    #window 3
    goto(35, -20)
    pendown()
    begin_fill()
    goto(65, -20)
    goto(65, -45)
    goto(35, -45)
    goto(35, -20)
    end_fill()


    fillcolor("black")
    pensize(1)
    penup()
    goto(0,0)

def drawCar():
    drawBody()
    drawWheels()
    drawBackWheel()
    drawWindow()

drawRoad()
drawStars(s=0)
drawCar()
goto(0, 20)
write("Happy Birthday! Dumbass.", move=False, align="center", font=("Arial", 20, "normal")) 

screen.mainloop()