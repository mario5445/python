from random import randrange, uniform

import turtle

t = turtle.Turtle()




def stvorec():
    t.penup()
    x = randrange(-200,100)
    y = randrange(-200,100)
    t.setpos(x, y)
    t.pendown()
    t.pencolor("blue")
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)


def trojuholnik():
    t.penup()
    x = randrange(-200, 100)
    y = randrange(-200, 100)
    t.setpos(x, y)
    t.pendown()
    t.pencolor("red")
    t.forward(30)
    t.left(150)
    t.forward(30)
    t.left(100)
    t.forward(20)


for i in range(randrange(5, 10)):
    stvorec()
    trojuholnik()









turtle.exitonclick()