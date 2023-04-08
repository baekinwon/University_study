import random

user = input("가위, 바위, 보?:")

select_com = random.choice(["가위","바위","보"])

print("COM: ",select_com)

if user == select_com:
    print("draw")
elif user == "가위" and select_com == "바위":
    print("lose")
elif user == "바위" and select_com == "보":
    print("lose")
elif user == "보" and select_com == "가위":
    print("lose")
else:
    print("win")
    
