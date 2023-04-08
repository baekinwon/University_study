import turtle
text = turtle.textinput("제목", "내용")

print(text)

turtle.bye()

#%%

import turtle

score = int(turtle.textinput("점수", "1~100"))

if score <= 100 and score >= 1:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    print("학점은",grade,"입니다.")
    
else:
    print("error")

turtle.bye()

#%%

import turtle

while True:
    text = turtle.textinput("선택", "t1 or t2")
    if text == "t1" or text == "t2":
        break

turtle.bye()

#%%

import turtle

turtle.color("green")
turtle.write("거북이")

turtle.exitonclick()
turtle.bye()

#%%

import turtle
turtle.shape("turtle")

font_a = ("굴림",20)
font_b = ("굴림",30)

turtle.write("거북이")
turtle.color("red")
turtle.fd(100)
turtle.write("고양이", font = font_a)
turtle.color("blue")
turtle.fd(100)
turtle.write("코끼리", font = font_b)

turtle.exitonclick()
turtle.bye()

#%%

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(0,200)
t.down()
t.goto(200,-200)

turtle.exitonclick()
turtle.bye()

#%%

import turtle

t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("blue")
t1.up()
t1.goto(0,200)
t1.down()
t1.goto(200,200)

t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()
t2.goto(200,-200)

turtle.exitonclick()
turtle.bye()
