#makes a tilted squre white on black
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

#change colors
turtle.color("white")
turtle.bgcolor("black")

#variables
n = 0 #so that the while only does it 4 times



turtle.right(45)# so that the caree is tilted
while n < 4:#square
    n += 1
    turtle.forward(150)
    turtle.right(90)




turtle.mainloop()
