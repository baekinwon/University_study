# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
t.shape("turtle")

home = int(input("집의 크기를 입력하시오 : "))
roof = input("지붕의 색을 입력하시오 : ")
wall = input("벽의 색을 입력하시오 : ")

for i in range(3):
    t.color(roof)
    t.forward(home)
    t.left(120)

t.right(90)
for j in range(3):
    t.color(wall)
    t.forward(home)
    t.left(90)

