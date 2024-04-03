import turtle
 
# Starting a Working Screen
ws = turtle.Screen()

# initializing a turtle instance
star = turtle.Turtle()
#color choosing
star.color("yellow")
#pensize choosing
star.pensize(5)
# executing loop 5 times for a star
for i in range(5):
 
        # moving turtle 100 units forward
        star.forward(100)
 
        # rotating turtle 144 degree right
        star.right(144)
#window stay open        
turtle.done()        