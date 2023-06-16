def escolhida(posCidade, posBebida):
    cidade = input('Digite o nome da cidade: ')
    bebida = int(input("Digite 1 para pitu, 2 para 51: "))
    for city in range(3):
        if posCidade[city] == cidade:
            print(posCidade)
        if bebida == 1:
           print(posBebida[1])
            


cidade = [[''],[''],['']]
bebida = [[0,0],[0,0],[0,0]]

for ci in range(3):
    cidade[ci] = input('Digite o nome da cidade: ')
    for c in range(2):
        bebida[ci][c] = int(input("Digite o valor da bebida: "))


print(cidade,bebida)

escolhida(cidade, bebida)




