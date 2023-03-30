import turtle
t = turtle.Turtle()
t.shape("turtle")

size1 = 200
size2 = 50
move_length = 10

t.dot(size1*2, "green")
t.dot(size2*2,"blue")

for i in range(0,301,10):
    print("move",i)
    t.undo()
    t.fd(move_length)
    t.dot(size2*2,"blue")
    d = t.distance(0,0)
    print("거북이 위치: ",t.pos())
    print("원점까지 거리(거북이): ",d)
    if d==0:
        print("충돌/동심원")
    elif size1-size2>d:
        print("충돌/내심존재")
    elif size1-size2 == d:
        print("충돌/내접")
    elif size1-size2<d<size1+size2:
        print("충돌/두접점")
    elif size1+size2==d:
        print("충돌/외접")
    elif size1+size2<d:
        print("비충돌")
    else:
        print("불가능")
turtle.exitonclick()
turtle.bye()