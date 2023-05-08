
import turtle

pos_list = [[100,100],
            [100,-100],
            [-100,100],
            [-100,-100]]

t = [turtle.Turtle("turtle") for i in range(4)]
for i in range(4):
    t[i].goto(pos_list[i][0],pos_list[i][1])

turtle.exitonclick()
turtle.bye()

#%%

from PIL import Image

image = Image.open('pet01.gif')
photo = image.convert('RGB')

photo.show()

#%%

from PIL import Image

image = Image.open('pet02.gif')
photo= image.convert('RGB')

photoAry = []
h = photo.height
w = photo.width
for i in range(h):
    for k in range(w):
        r,g,b = photo.getpixel((i,k))
        value = (r+g+b)//3
        photoAry.append(value)

dataAry = photoAry[:]
dataAry.sort()
midValue = dataAry[h*w//2]

for i in range(len(photoAry)):
    if photoAry[i]<=midValue:
        photoAry[i]=0
    else:
        photoAry[i]=255
        
pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r=g=b=photoAry[pos]
        pos+=1
        px[i,k] = (r,g,b)
    
photo.show()

#%%

import turtle
t = turtle.Turtle("turtle")

x = 0
y = 0
x_vel = 0
y_vel = 3

for i in range(100):
    x += x_vel
    y += y_vel
    t.goto(x,y)

turtle.exitonclick()
turtle.bye()

#%%

pos_list = [[0,0],
            [0,0],
            [0,0]]

vel_list = [[2,0],
            [0,2],
            [2,2]]

for step in range(10):
    for i in range(len(pos_list)):
        pos_list[i][0]+=vel_list[i][0]
        pos_list[i][1]+=vel_list[i][1]
    print(pos_list)
    
#%%

import turtle

pos_list = [[0,0],
            [0,0],
            [0,0]]

vel_list = [[0,2],
            [-2,0],
            [-2,2]]

t = [turtle.Turtle("turtle") for i in range(len(pos_list))]

for step in range(100):
    for i in range(len(pos_list)):
        pos_list[i][0]+=vel_list[i][0]
        pos_list[i][1]+=vel_list[i][1]
        
        t[i].goto(pos_list[i][0],pos_list[i][1])

turtle.exitonclick()
turtle.bye()

#%%

import turtle

tline = turtle.Turtle()

sc_w = 400
sc_h = 300

tline.up()
tline.goto(sc_w/2,sc_h/2)
tline.down()

tline.goto(-sc_w/2,sc_h/2)
tline.goto(-sc_w/2,-sc_h/2)
tline.goto(sc_w/2,-sc_h/2)
tline.goto(sc_w/2,sc_h/2)

screen = turtle.Screen()
screen.exitonclick()

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

screen = turtle.Screen()
screen.exitonclick()

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
vel = [5,1]

t.goto(loc[0],loc[1])

for i in range(200):
    loc[0]+=vel[0]
    loc[1]+=vel[1]
    
    t.goto(loc[0],loc[1])
    
    if loc[0] >= sc_w/2 or loc[0]<=-sc_w/2:
        vel[0] = -vel[0]
    if loc[1] >= sc_h/2 or loc[1] <= -sc_h:
        vel[1] = -vel[1]
    
turtle.exitonclick()
turtle.bye()
