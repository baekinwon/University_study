import random

lottoNum = []

for i in range(1,7):
    while True:
        pickNum = random.randrange(1,46)
        if pickNum in lottoNum:
            continue
        else:
            lottoNum.append(pickNum)
            break

print("로또번호")
print(lottoNum)