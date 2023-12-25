import turtle

wd = turtle.Screen()
trunk = turtle.Turtle()

wd.bgcolor("sky blue")

tree = turtle.Turtle()
tree.color("forest green")

#create a tree segment
def make_tree_segment(size,top_position):
    
    tree.begin_fill()
    tree.setposition(0, top_position)
    tree.setposition(size,top_position -size)
    tree.setposition(-size,top_position -size)
    tree.setposition(0,top_position)
    tree.end_fill()

#create a tuple
tree_position = ((50, 20), (80, 0), (120, -30), (150, -60))

#for loop which repeat the program as many times as there are items in tree_position
for size, top_position in tree_position:
    make_tree_segment(size, top_position)



def make_tree_trunk():
    trunk.penup()
    trunk.setx(0)
    trunk.sety(-220)
    trunk.pendown()
    #trunk.position(90, 40) #position is not working yet
    trunk.color("brown")
    trunk.pensize(50)
    trunk.begin_fill()
    trunk.right(90)
    trunk.forward(40)
    trunk.right(90)
    trunk.end_fill()

make_tree_trunk()

turtle.done()