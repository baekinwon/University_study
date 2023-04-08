import random
import turtle

t1_sum = 0
t2_sum = 0

while True:
    win_user = turtle.textinput("주사위 게임","t1 or t2")
    if win_user == "t1" or win_user == "t2":
        break

worl = ""

while True:
    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)
    t1_sum+=t1
    t2_sum+=t2
    print("t1: ",t1_sum," vs ","t2: ",t2_sum)
    if t1_sum >= 30 or t2_sum >=30:
        if t1_sum > t2_sum:
            print("t1 승리")
            worl = "t1"
        elif t1_sum == t2_sum:
            print("무승부")
        else:
            print("t2 승리")
            worl = "t2"
        break;

if win_user == worl:
    print("맞췄습니다.")
else:
    print("틀렸습니다.")

turtle.bye()