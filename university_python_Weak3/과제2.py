# -*- coding: utf-8 -*-

mon = int(input("투입한 돈 : "))

obj = int(input("물건의 가격 : "))

gu = mon-obj
print("거스름돈 : ",gu)
fi = gu//500
print("500원 동전의 개수: ",fi)
print("100원 동전의 개수: ",(gu-fi*500)//100)