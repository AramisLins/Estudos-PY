# media com if aprovado

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
soma = num1 + num2 + num3
media = soma / 3
if media >= 5 :
  print("aprovado")
else :
  print("Reprovado")

#validade de senha

senha = int(input("digite sua senha: "))
snvld = 123456
if senha == 123456:
  print("Acesso Liberado")
else:
  print("Acesso Negado")

#3 valores inteiros

num1 = int(input("digite o 1 valor: "))
num2 = int(input("digite o  2 valor: "))
num3 = int(input("digite o 3 valor: "))
soma = num1 + num2
if soma < num3:
  print("C")
else:
  print("c")

#salario e aumento

salario = float(input("digite o seu salario: "))
if salario <= 300:
  aumento1  = salario * 1.35
  print("seu novo salario é: ", aumento1)
else:
  aumento2 = salario * 1.15
  print("seu novo salario é: ", aumento2)

#3 numeros e dizer o maior

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
if num1 == num2 == num3:
  print("todos iguais")
elif num1 > num2 and num1 > num3:
  print("primeiro numero maior")
elif num2 > num1 and num2 > num3:
  print("segundo numero maior")
else:
  print("terceiro numero maior")

#norte e nordeste

sigla = input("digite a sigla do seu estado: ").lower()
if sigla == "pb" or sigla == "pe":
  print("nordeste")
elif sigla == "sp" or sigla == "rj":
  print("Sudeste")
else:
  print("Norte ou centro")





  