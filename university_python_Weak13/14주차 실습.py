numList = []
for num in range(1,6):
    numList.append(num)
print(numList)

#%%

numList=[num for num in range(1,6)]
print(numList)

#%%

numList=[num+2 for num in range(1,6)]
print(numList)

#%%

numList=[num for num in range(1,21) if num %2==0]
print(numList)