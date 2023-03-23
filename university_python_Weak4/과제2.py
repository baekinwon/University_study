# -*- coding: utf-8 -*-

import turtle
t = turtle.Turtle()
t.shape("turtle")

x = 300
y = 100
size1 = 200
size2 = 100

print("원점에서의 거리(계산):",t.distance(x,y))

t.dot(size1*2,"green")
t.fd(x)
t.left(90)
t.fd(y)
t.dot(size2*2,"yellow")

print("거북이 위치: ",t.pos())
print("원점까지 거리(거북이): ",t.distance(0,0))

print("충돌 판단 => ")

if t.distance(0,0)==0 or size1-size2 > t.distance(0,0):
    print("충돌/내부위치")
elif size1-size2 == t.distance(0,0)or  size1-size2< t.distance(0,0) <size1+size2 or size1+size2==t.distance(0,0):
    print("충돌/접점존재")
else:
    print("비충돌")

turtle.exitonclick()
turtle.bye()