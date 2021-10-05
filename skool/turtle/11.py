#doesnt work
import turtle
import math

#start up turtle
turtle.shape("turtle")
turtle.screensize(1000, 1000)
turtle.reset()
turtle.clear()

print("1 pour spirale 2 pour etoile 3 pour autre")
choice = input()





def sprial(size):
    for i in range(0, 9):
        size += 30
        for i in range(0, 2):
            turtle.forward(size)
            turtle.left(90)

def star(size):
    for i in range(3):
        forward(size)
        left(60)
        forward(size)
        left(120)

def main(choice):
    if choice == 1:
        spiral(40)
    elif choice == 2:
        star(40)

turtle.mainloop()
