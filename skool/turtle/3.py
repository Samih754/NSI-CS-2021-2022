#makes a series of lines
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

size = 30
turtle.up()
turtle.goto(-120, 0)
turtle.down()

for i in range(0, 4):
    turtle.forward(size)
    turtle.up()
    turtle.forward(size)
    turtle.down()



turtle.mainloop()
