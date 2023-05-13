import turtle
import time

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

t = [turtle.Turtle("circle") for i in range(2)]

loc = [[0,0],[0,0]]
vel = [[5,-5],[5,5]]

t[0].goto(loc[0][0],loc[0][1])
t[1].goto(loc[1][0],loc[1][1])

startTime = time.time()

for i in range(200):
    for j in range(2):
        loc[j][0]+=vel[j][0]
        loc[j][1]+=vel[j][1]
        t[j].goto(loc[j][0],loc[j][1])
        if loc[j][0] >= sc_w/2 or loc[j][0]<=-sc_w/2:
            vel[j][0] = -vel[j][0]
        if loc[j][1] >= sc_h/2 or loc[j][1] <= -sc_h/2: 
            vel[j][1] = -vel[j][1]

ti = turtle.Turtle()
ti.write(time.time()-startTime)

turtle.exitonclick()
turtle.bye()