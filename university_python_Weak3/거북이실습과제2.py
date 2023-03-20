# -*- coding: utf-8 -*-
x = input("첫 번째 정수를 입력하시오 : ")
y = input("두 번째 정수를 입력하시오 : ")

print(x,"+",y,"=",x+y)

#%%

x_str = input("첫 번째 정수를 입력하시오 : ")
y_str = input("두 번째 정수를 입력하시오 : ")

x = int(x_str)
y = int(y_str)

print(x,"+",y,"=",x+y)

#%%
import turtle

t = turtle.Turtle()
t.shape("turtle")

col = ["blue","red","green"]

fo = ["처음","다음","마지막"]

for i in range(3):
    t.color(col[i])
    forw = int(input(fo[i]+" 이동할 거리를 입력하시오 : "))
    t.forward(forw)

#%%

turtle.bye()