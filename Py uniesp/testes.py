# def calcular_imc(peso, altura):
#     imc = peso / (altura*2)
#     return imc

# pessoas = []
# i = 0
# cadastrar = int(input("quantas vezes quer cadastrar? "))
# for i in range(cadastrar):
#     nome = input(f"Digite o nome da pessoas{i + 1}:")
#     idade = int(input(f"Digite a idade da pessoa{i + 1}:"))
#     peso = float(input(f"Digite o peso da pessoa{i+1}:"))
#     altura = float(input(f"Digite a altura da pessoa{i+1}"))

#     cadastro = (nome, idade, peso, altura)
#     pessoas.append(cadastro)

#     imc = calcular_imc(peso,altura)

#     print(pessoas)


nome = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade do produto: "))
valor = float(input("Digite o valor de venda: "))

valorPago = float(input("Qual valor foi pago ? "))

if(valorPago > valor):
    res = valorPago - valor
    print(f"O troco ficou de :{res}R$")
elif(valorPago == valor):
    print("Pago com sucesso !!!")
else:
    res = valor - valorPago
    print(f"Valor insuficiente, pague {res} no caixa")