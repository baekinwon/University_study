sum = 0
for i in range(101):
    sum += i
print("1부터 100까지의 합은,",sum,"입니다.")

#%%

import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.forward(100)
    t.right(144)
turtle.exitonclick()

#%%

password = ""

while password != "python":
    password = input("암호를 입력하시오: ")
print(">>로그인 성공")

#%%

password = ""

while password != "blue" and password != "red":
    password = input("암호를 입력하시오: ")
print(">>로그인 성공")

#%%

for i in range(5):
    for j in range(10):
        print("*",end = " ")
    print()

#%%

for i in range(5):
    for j in range(i+1):
        print("*", end= " ")
    print()
    
#%%

sign = True
light = "red"

while sign:
    light = input("신호등의 색상은?:")
    if light == "blue":
        sign = False
print("전진!!")

#%%
while True:
    light = input("신호등의 색상은?:")
    if light == "blue":
        break
print("전진!!")

#%%

for n in range(10):
    if n%2==0:
        continue
    print(n)
    if n > 5:
        break
    
#%%

answer = 5

while True:
    number = int(input("정답은?: "))
    if answer == number:
        print("정답입니다.")
        break
    elif answer>number:
        print("정답은 더 높은 수 입니다.")
    else:
        print("더 낮은 수 입니다.")
        