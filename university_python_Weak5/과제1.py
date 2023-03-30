# -*- coding: utf-8 -*-

age = int(input("나이 : "))
getmoney = 0
if age > 20:
    getmoney = 10000
else:
    getmoney = 5000
sum_money = 0
while True:
    money = int(input("돈 : "))
    sum_money+=money
    if sum_money>=getmoney:
        print(">>>거스름돈 : ",sum_money-getmoney)
        print("입장가능")
        break
    else:
        print("추가필요금액 : ",getmoney-sum_money)
        print("입장불가")
    
    