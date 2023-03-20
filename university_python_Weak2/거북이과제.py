# -*- coding: utf-8 -*-
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")



num = 0
for i in range(4):
    t.forward(100)
    t.left(90)
    if num == 0:
        t.color("red")
    elif num == 1:
        t.color("green")
    else:
        t.color("yellow")
    num+=1
