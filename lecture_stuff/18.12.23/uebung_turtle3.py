import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5

size = 6
for i in range(8):
    size += 20
    sqrfunc(size)

turtle.done()