valores = [[0,0],[0,0],[0,0]]
valor = 0
numNegativo = 0

for l in range(3):
    for c in range(2):
        valores[l][c] = int(input("Digite o valor"))
        if valores[l][c] > 0:
            valor = valor + valores[l][c]
        else :
            numNegativo += 1
            
print(valor)
print(numNegativo)