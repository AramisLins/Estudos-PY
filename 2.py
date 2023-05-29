valores = [[0,0,0],[0,0,0]]
valor = 0

for l in range(2):
    for c in range(3):
        valores[l][c] = int(input("Digite o valor"))
        if valores[l][c] > 0:
            valor = valor + valores[l][c]
            
print(valor)