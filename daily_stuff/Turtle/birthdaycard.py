import turtle
import random

bg= turtle.Screen()
bg.bgcolor("black")

cake = turtle.Turtle()
cake.shape("turtle")
cake.speed()

def line(x1,y1,x2,y2,color,pensize):
    cake.penup()
    cake.goto(x1,y1)
    cake.color(color)
    cake.pensize(pensize)
    cake.pendown()
    cake.goto(x2,y2)
    cake.penup()

snow_colors = ["white", "blue", "silver", "light yellow", "light blue",  "purple", "grey", "magenta", 'green', 'orange', 'gold', 'red', 'red']

line(-190, -180, 190, -180,random.choice(snow_colors),6)
line(-160,-150, 160, -150, random.choice(snow_colors), 6)
line(-130,-120, 130, -120, random.choice(snow_colors), 6)

#draw cake
cake.goto(-70,-110)
cake.begin_fill()
cake.pendown()
cake.color("white")
cake.goto(50,-110)
cake.left(90)
cake.forward(60)
cake.left(90)
cake.forward(125)
cake.left(90)
cake.forward(60)
cake.penup()
cake.end_fill()

#draw candles
def candle(x, color):
    cake.goto(x,-40)
    cake.color(color)
    cake.pendown()
    cake.pensize(3)
    cake.goto(x, -20)
    cake.penup()

candle(-60,"yellow")
candle(-40,"yellow")
candle(-20,"yellow")
candle(0,"yellow")
candle(20,"yellow")
candle(40,"yellow")

#print message 
cake.goto(-200,30)
cake.color("white")
cake.pendown()
cake.write("Happy Birthday!", font=("Verdana",
                                    36, "bold"))

cake.penup()
cake.goto(-250,250)

turtle.done()