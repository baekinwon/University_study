# -*- coding: utf-8 -*-

import turtle
t = turtle.Turtle()
t.shape("turtle")

#%%

size = 50
angle = 90

col = ["blue","red","green","yellow"]
for i in range(4):
    t.color(col[i])
    t.forward(size)
    t.left(angle)

#%%

turtle.bye()