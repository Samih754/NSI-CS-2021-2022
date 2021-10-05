#makes squares and triangles with purple and orange coloring
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

print("a")
a = int(input())
print("n")
n = int(input())

turtle.speed(10)

def triangle(a):
    for i in range(3):
        turtle.forward(a)
        turtle.left(120)

def square(a):
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)



for i in range(n):
    turtle.color("purple", "orange")
    turtle.width(3)
    turtle.begin_fill()
    triangle(a)
    turtle.end_fill()
    turtle.up()
    turtle.forward((a) + 10)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.down()


    turtle.color("purple", "orange")
    turtle.width(3)
    turtle.begin_fill()
    square(a)
    turtle.end_fill()
    turtle.up()
    turtle.forward(a + 10)
    turtle.right(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.down()


turtle.mainloop()
