#creates a square with a for i in range() loop
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

size = 30
for i in range(0, 4):
    turtle.forward(size)
    turtle.right(90)

turtle.mainloop()
