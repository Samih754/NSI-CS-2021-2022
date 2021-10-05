#creates  spiral
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

size = 0
for i in range(0, 9):
    size += 30
    for i in range(0, 2):
        turtle.forward(size)
        turtle.left(90)



turtle.mainloop()
