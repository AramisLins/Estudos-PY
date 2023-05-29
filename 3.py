numeros =[]

for i in range(10):
    num = int(input(f"Digite o {i+1} numero: "))
    numeros.append(num)
    
    
numeros.sort(reverse=True)
print(numeros)