import random
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0
for x in range(20):
    num = random.randint(1,6)
    if num == 1:
        contador1 += 1 
    elif num == 2:
        contador2 += 1
    elif num == 3:
        contador3 += 1
    elif num == 4:
        contador4 += 1
    elif num == 5:
        contador5 += 1
    elif num == 6:
        contador6 += 1

print(contador1)
print(contador2)
print(contador3)
print(contador4)
print(contador5)
print(contador6)