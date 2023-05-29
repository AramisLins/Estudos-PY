numInteiro = []
numPar = []
numImpar = []

for x in range(20):
    num = int(input(f"Digite o {x + 1} numero: "))
    numInteiro.append(num)
    if num % 2 == 0:
        numPar.append(num)
    else:
        numImpar.append(num)
        
print(numImpar)
print(numInteiro)
print(numPar)