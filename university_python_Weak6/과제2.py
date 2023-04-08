import random

t1_sum = 0
t2_sum = 0

while True:
    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)
    t1_sum+=t1
    t2_sum+=t2
    print("t1: ",t1_sum," vs ","t2: ",t2_sum)
    if t1_sum >= 30 or t2_sum >=30:
        if t1_sum > t2_sum:
            print("t1 승리")
        elif t1_sum == t2_sum:
            print("무승부")
        else:
            print("t2 승리")
        break;