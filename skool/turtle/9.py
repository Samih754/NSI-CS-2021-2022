#cretes a hexagon
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

for i in range(6):
    triangle(40)
    turtle.forward(40)
    turtle.left(60)

turtle.mainloop()
