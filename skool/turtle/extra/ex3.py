#makes wierd squares
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

turtle.speed(1)
print('a=?: ')
a = int(input())
print("n=?
n = int(input())

def square(a):
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)

for i in range(n):
    square(a)
    turtle.up()
    turtle.forward(a)
    turtle.forward(a /4)
    turtle.down()
    a = a * 1.25

turtle.mainloop()
