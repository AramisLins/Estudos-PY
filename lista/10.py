def divisao(num1, num2):
    res = num1 / num2
    print(res)
    
def multi(num1, num2):
    res = num1 * num2
    print(res)
    
def media(num1, num2):
    media = (num1 + num2) / 2
    print(media)

def sub(num1, num2):
    res = num1 - num2
    print(res)
    
num1 = int(input('Digite o 1 numero: '))
num2 = int(input('digite o 2 numero: '))
simbolo = int(input("Digite o codigo da operação: "))
if simbolo == 1:
    media(num1, num2)
if simbolo == 2:
    sub(num1, num2)
if simbolo == 3:
    multi(num1, num2)
if simbolo == 4:
    divisao(num1, num2)
