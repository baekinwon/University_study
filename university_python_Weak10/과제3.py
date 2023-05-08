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
vel = [0,5]

t.goto(loc[0],loc[1])

for i in range(200):
    loc[0]+=vel[0]
    loc[1]+=vel[1]
    
    t.goto(loc[0],loc[1])
    
    if loc[1] >= sc_h/2 or loc[1] <= -sc_h/2:
        vel[1] = -vel[1]
    
turtle.exitonclick()
turtle.bye()
