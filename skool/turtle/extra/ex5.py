#doesnt work
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

ang = 0

print("n, d ,a")
n = int(input())
d = int(input())
a = int(input())

def rayon(n, d):
    angle = 360 / n

    for r in range(n):
        ang = ang + (360 / n)
        turtle.forward(d)
        turtle.right(angle)
        turtle.goto(0,0)


turtle.mainloop()
