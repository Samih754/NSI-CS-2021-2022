#creates a function to make the square.
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

square(30)


turtle.mainloop()
