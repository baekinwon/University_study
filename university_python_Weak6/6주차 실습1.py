import random
num_int = random.randint(1,10)
print(num_int)

num_float = random.random()
print(num_float)

#%%

import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(100):
    num_int = random.randint(1,5)
    if num_int == 1:
        num1+=1
    elif num_int == 2:
        num2+=1
    elif num_int == 3:
        num3+=1
    elif num_int == 4:
        num4+=1
    elif num_int == 5:
        num5+=1

print(num1, num2, num3, num4, num5)

#%%

import random

for i in range(30):
    num_int = random.randint(1,5)
    print(" "*(num_int-1),num_int)
