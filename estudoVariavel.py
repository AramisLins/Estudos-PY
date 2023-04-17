#soma 
num1 = int(input("Digite a 1 idade: "))
num2 = int(input("digite a 2 idade: "))
num3 = int(input("digite a 3 idade: "))
num4 = int(input("digite a 4 idade: "))
num5 = int(input("digite a 5 idade: "))
num6 = int(input("digite a 6 idade: "))
num7 = int(input("digite a 7 idade: "))
num8 = int(input("digite a 8 idade: "))
num9 = int(input("digite a 9 idade: "))
num10 = int(input("digite a 10 idade: "))
soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
media = soma / 10
print("A media das idades é: ", media)

#media de 3 notas float
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
soma = num1 + num2 + num3
media = soma / 3
print("media foi: ", media)

#rea do retangulo
num1 = float(input("Digite a base: "))
num2 = float(input("Digite a altura: "))
#num3 = float(input("Digite a terceira nota: "))
area = num1 * num2
print("A valor da área é: ", area)

#idade do usuario
num1 = int(input("digite o ano que nasceu: "))
idade = 2023 - num1
print("vc tem", idade ,"anos")


#preço e quantidade produto

num1 = float(input("digite o preço do produto: "))
num2 = float(input("digite a quantidade adiquirida: "))
valorTotal = num1 * num2
print("o Valor total foi: ", valorTotal)

#aumentos de salario
salario = float(input("digite o seu salario: "))
aumento1 = salario * 1.25
aumento2 = salario * 1.50
aumento3 = salario * 1.75
print("primeiro aumento: ", aumento1)
print("segundo aumento: ", aumento2)
print("terceiro aumento: ", aumento3)


#altura do trapezio 
baseM = float(input("Digite a base maior: "))
basem = float(input("Digite a base menor: "))
altura = float(input("digite a altura: "))
area = ((baseM + basem) / 2) * altura
print("area do trapezio é: ", area)

#idade com if cnh
idade = int(input("digite sua idade: "))
if idade >= 18:
  print("apto")
else :
  print("inapto")


  
