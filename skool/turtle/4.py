#makes a series of lines whilst writing the position of it iver them
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

turtle.up()
turtle.goto(-200, 0)
turtle.down()
size = 15
for i in range(1, 15):
    turtle.write(i)
    turtle.forward(size)
    turtle.up()
    turtle.forward(size)
    turtle.down()

turtle.mainloop()
