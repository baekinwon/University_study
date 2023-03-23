# -*- coding: utf-8 -*-

score = 90
if score == 100:
    print("만점입니다!")
print("수고하셨습니다.")

#%%

num = int(input("당신의 나이를 입력하세요:"))
if num < 20:
    print(">>>입장료 : 5000원")
else:
    print(">>>입장료 : 10000원")
    
#%%

num = int(input("양의 정수:"))

if num%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#%%

age = 15
height = 100

if age >= 10:
    if height >= 110:
        print(">>>탑승가능합니다.")
    else:
        print(">>>키제한으로 탑승불가능합니다.")
        print(">>>죄송합니다.")
else:
    print(">>>나이제한으로 탑승불가능합니다.")
    print(">>>죄송합니다.")
    
#%%

age = 15
height = 190

if age >= 10 and height >= 110:
    print("탑승가능")
else:
    print("탑승불가")
    print("죄송합니다.")
    
#%%

age = int(input("나이:"))

money = int(input("돈:"))

if age < 20 : 
    if money>5000:
        money-=5000
        print(">>>입장가능")
        print(">>>거스름돈:",money)
    else:
        print("입장불가")
        print("추가필요금액:",5000-money)
elif age >= 20:
    if money>10000:
        money-=10000
        print(">>>입장가능")
        print(">>>거스름돈:",money)
    else:
        print("입장불가")
        print("추가필요금액:",10000-money)