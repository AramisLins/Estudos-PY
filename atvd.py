#PRIMEIRA QUESTÃO
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
c = float(input("Digite o terceiro numero: "))
soma = a + b
if soma < c :
  print("a + b menor que c")
else:
  print("igual ou maior que C")


#SEGUNDA QUESTÃO
num1 = int(input("Digite o seu numero: "))
if num1%2 == 0:
  print("Numero par")
else:
  print("Numero impar")

#TERCEIRA QUESTÃO
a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
if a == b:
  c = a + b
  print("O valor de da soma ficou: ", c)
else:
  c = a * b
  print("O valor da multiplicação ficou: ", c)



#QUARTA QUESTÃO
num1 = int(input("Digite um numero: "))
if num1 > 0:
  print("O valor ficou: ", num1 * 2)
else:
  print("O valor ficou: ", num1 * 3)

#QUINTA QUESTÃO
num1 = int(input("Digite o seu numero: "))
if num1%2 == 0:
  par = num1 + 5
  print("Numero par ficou: ", par)
else:
  impar = num1 + 8
  print("Numero impar ficou: ", impar)

#SEXTA QUESTÃO
print("Digite 3 valores diferentes, caso algum seja igual, vai da invalido")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3= int(input("Digite o terceiro numero: "))

if num1 > num2  and num1 > num3 and num2 > num3:
    print(f'A ordem decrescente é {num1} , {num2} e {num3}')
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f'A ordem decrescente é {num1} , {num3} e {num2}')
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f'A ordem decrescente é {num2} , {num1} e {num3}')
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f'A ordem decrescente é {num2} , {num3} e {num1}')
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f'A ordem decrescente é {num3} , {num1} e {num2}')
elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f'A ordem decrescente é {num3} , {num2} e {num1}')
else:
  print("invalido")


#SETIMA QUESTÃO
altura = float(input("Digite sua altura: "))
print("Digite 1 para Masculino \nDigite 2 para feminino")
sexo = int(input("-"))
if sexo == 1:
  masc = (72.7 * altura) - 58
  print("peso ideal é: ", masc)
elif sexo == 2:
  fem = (62.1 * altura) - 44.7
  print("peso ideal é: ", fem)
else:
  print("Opção invalida")

#OITAVA QUESTÃO
peso = float(input("digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
  print("Abaixo do peso")
elif 18.5 <= imc < 25:
  print("Peso normal")
elif 25 <= imc < 30:
  print("Acima do peso")
elif imc >= 30:
  print("Obeso")

#NONA QUESTÃO
produto = float(input("Digite o valor do produto: "))
print("Formas de pagamento: \n1-À vista em dinheiro ou cheque, recebe 10% de desconto!\n2-À vista no cartão de credito, recebe 15% de desconto!\n3- Em duas vezes, preço normal de etiqueta sem juros\n4- Em duas vezes, preço normal de etiqueta mais juros de 10%")
codigo = int(input("Digite a opção desejada: "))
if codigo == 1:
  calc = produto - (produto * 10/100)
  print("O valor ficou, ", calc)
elif codigo == 2:
  calc = produto - (produto * 15/100)
  print("O valor ficou: ", calc)
elif codigo ==3 :
  print("O valor ficou o mesmo: ", produto)
elif codigo == 4:
  calc = produto * 1.10
  print("O valor ficou: ", calc)
else:
  print("Opção Invalida!!")

#DECIMA QUESTÃO
rgm = int(input("Digite seu numero de identificação: "))
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
me = float(input("Qual sua Media dos exercicios: "))
ma = (num1 + num2 *2 + num3 * 3 + me) / 7
if ma >= 90:
  print("Conceito A, aprovado")
elif 75 >= ma < 90 :
  print("Conceito B, aprovado")
elif 60 >= ma < 75:
  print("Conceito C, aprovado")
elif 40 >= ma < 60:
  print("Conceito D, reprovado")
elif ma < 40 :
  print("conceito E, reprovado")
