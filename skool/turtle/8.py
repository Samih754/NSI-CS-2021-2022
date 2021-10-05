#draws a square and then a tringle, it's disgusting cause i refused to use right() out of personal convictions
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

def square(size):
    for i in range(0, 4):
        turtle.forward(size)
        turtle.right(90)

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

turtle.up()
turtle.goto(-100, 0)
turtle.down()
for i in range(3):
    square(30)
    turtle.up()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    triangle(30)
    turtle.up()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.down()




turtle.mainloop()
