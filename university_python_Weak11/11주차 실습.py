import datetime

nowTime = datetime.datetime.now()
print(nowTime)

#%%

from datetime import date

Memorial = date(2004,1,2)
nowTime = date.today()
timeDiff = nowTime - Memorial
print(timeDiff)

#%%

import datetime

Memorial = datetime.datetime(2004,1,2,00,00)
nowTime = datetime.datetime.now()
timeDiff = nowTime - Memorial
print(timeDiff)

#%%

from datetime import datetime

startTime = datetime.now()

while True:
    currTime = datetime.now()
    print((currTime - startTime).seconds)

#%%

from datetime import datetime

startTime = datetime.now()

while True:
    currTime = datetime.now()
    timeDiff = currTime - startTime
    print(timeDiff.microseconds)
    #print(timeDiff.microseconds/1000)

#%%

import time

startTime = time.time()

while True:
    timeDiff = (time.time() - startTime)
    print('{:.2f}'.format(timeDiff))
    if timeDiff>10:
        break

#%%

import time

startTime = time.time()

while True:
    timeDiff = (time.time() - startTime)
    print(timeDiff)
    time.sleep(1.0)
    if timeDiff>10:
        break

#%%

import turtle

t = turtle.Turtle("turtle")

for i in range(3):
    t.fd(100)
    t.left(120)
    time.sleep(0.5)

turtle.exitonclick()
turtle.bye()

#%%

import pygame

#%%

import turtle

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(sc_w/2,sc_h/2)
    tline.down()

    tline.goto(-sc_w/2,sc_h/2)
    tline.goto(-sc_w/2,-sc_h/2)
    tline.goto(sc_w/2,-sc_h/2)
    tline.goto(sc_w/2,sc_h/2)

sc_w = 400
sc_h = 300


outline()

t = turtle.Turtle()
t.shape("circle")

loc = [0,0]
vel = [5,0]

t.goto(loc[0],loc[1])

for i in range(50):
    loc[0]+=vel[0]
    loc[1]+=vel[1]
      
    if loc[0] >= sc_w/2:
        loc[0] = sc_w/2*2-loc[0]
        vel[0] = -vel[0]
    
    t.goto(loc[0],loc[1])
    
turtle.exitonclick()
turtle.bye()

#%%

import turtle

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(sc_w/2,sc_h/2)
    tline.down()

    tline.goto(-sc_w/2,sc_h/2)
    tline.goto(-sc_w/2,-sc_h/2)
    tline.goto(sc_w/2,-sc_h/2)
    tline.goto(sc_w/2,sc_h/2)

sc_w = 400
sc_h = 300


outline()

t = turtle.Turtle()
t.shape("circle")

loc = [100,100]
vel = [4,-4]

t.goto(loc[0],loc[1])

for i in range(100):
    loc[0]+=vel[0]
    loc[1]+=vel[1]
    
    t.goto(loc[0],loc[1])
    
    if loc[0] >= sc_w/2 or loc[0]<=-sc_w/2:
        vel[0] = -vel[0]
    if loc[1] >= sc_h/2 or loc[1] <= -sc_h/2: 
        vel[1] = -vel[1]
    
turtle.exitonclick()
turtle.bye()