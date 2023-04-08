import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")


t1.color("blue")
t1.up()
t1.goto(0,150)
t1.down()
for i in range(4):
    t1.fd(100)
    t1.left(90)

t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()
for i in range(4):
    t2.fd(100)
    t2.left(90)
    
t3.color("green")
t3.up()
t3.goto(200,0)
t3.down()
for i in range(4):
    t3.fd(100)
    t3.left(90)
    
turtle.exitonclick()
turtle.bye()