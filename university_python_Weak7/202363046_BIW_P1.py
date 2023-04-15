import turtle

t = turtle.Turtle()
t.shape("turtle")

def square_move(x,y,length):
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.fd(length)
        t.left(90)
        
square_move(0,100,50)
square_move(100,50,100)
square_move(-100,-100,150)

turtle.exitonclick()
turtle.bye()