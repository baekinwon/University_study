import random

number = [0,0,0,0,0,0,0,0,0,0]

for i in range(100):
    ran = random.randint(0, 9)
    number[ran] +=1
    
print(number)

#%%

import turtle

result = 0
input_list = []

while True:
    num = int(turtle.textinput("누적", "1~10, 0:종료"))
    input_list.append(num)
    if num == 0:
        break
    result+=num
    print(result)

print(input_list)
turtle.bye()

#%%

def get_sum(start,end=10):
    sum = 0
    for i in range(start,end+1):
        sum+=i
    print("sum = ",sum)
    
get_sum(1)
get_sum(1,20)
get_sum(5)
get_sum(5,10)

#%%

import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(100)
        t.left(90)

square(100)
t.up()
t.goto(200,0)
t.down()
square(100)

turtle.exitonclick()
turtle.bye()

#%%

result = 0

def rectangular_area():
    global result
    result = x * y
    
x = 3
y = 4
rectangular_area()
print(result)

#%%

def calc(x,y):
    return x-y

print(calc(10,20))
print(calc(20,10))

print(calc(x=10,y=20))
print(calc(y=20,x=10))

#%%

# 시험문제 나옴
def func1(x,y,z):
    print(x * y + z)
    return x*y+z

func1(1,3,5)
func1(y=7,z=5,x=2)
func1(z=2,x=4,y=5)
func1(5,z=10,y=2)
#func1(z=10,5,x=2)
#func1(5,x=2,z=20)