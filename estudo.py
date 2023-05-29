#criar uma matriz de forma manual sem laço de repetição

numeros= [
    [int(input("Digite a primeirda idade: ")), int(input("Digite a segunda idade: "))],
    [int(input("Digite a terceira idade: ")), int(input("Digite a quarta idade: "))]
    
]

print(numeros)

#iniciando a matriz sem o append

numeros = [[0,0],[0,0]]

for l in range(2):
    for c in range(2):
        numeros[l][c] = int(input("Digite um número: "))
        
print(numeros[1])

#faça um programa que receba o peso de 9 pessoas em uma matriz 3x3 e escreva o maior peso digitado


pesos = [[0,0,0],[0,0,0],[0,0,0]]
maiorPeso = 0

for l in range(3):
    for c in range(3):
        pesos[l][c] = float(input("Digite o seu peso: "))
        if (maiorPeso < pesos[l][c]):
            maiorPeso = pesos[l][c]
        
        
print(maiorPeso)

