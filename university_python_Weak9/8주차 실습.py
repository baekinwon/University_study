fibo_list = [1,1]

for n in range(10):
    fibo_new = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(fibo_new)

print(fibo_list)

#%%

List = ['A','B','C','D','E','F']

print(List[::2])
print(List[-2::-2])
print(List[::-2])
print(List[-3::-2])

#%%

List = [5,4,2,7,0,-5]

List.sort()
print(List)
List.sort(reverse = True)
print(List)

#%%

import turtle

aList = []

for i in range(4):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)

for i in range(4):
    aList[i].left(i*90)
    
for i in aList:
    i.fd(100)

turtle.exitonclick()
turtle.bye()

#%%

import turtle

aList = []

for i in range(6):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)

for i in range(6):
    aList[i].left(i*60)
    
for dist in [50,100,50,50]:
    for a in aList:
        a.fd(dist)
        a.left(30)

turtle.exitonclick()
turtle.bye()