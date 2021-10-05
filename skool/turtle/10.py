#draws multipls hexagons
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

print("length?: ")
length = int(input())

print("times?: ")
times = int(input())

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

for i in range(20):
    for i in range(0, 6):
        triangle(length)
        turtle.right(60)
    length += times


turtle.mainloop()
