import turtle

def change(mon,cont):
    if cont == "미국":
        TBR = 1117.5
    elif cont == "일본":
        TBR = 1022.56
    elif cont == "유럽연합":
        TBR = 1343.24
    else:
        print("잘못된 국가 입력입니다.")
        return 0
    result = mon/TBR
    return result

while True:
    money = float(turtle.textinput("환전계산기", "KRW"))
    contry = turtle.textinput("환전계산기","국가")
    
    if money == 0:
        break
    
    change_value= change(money, contry)
    print(change_value)
    
turtle.bye()