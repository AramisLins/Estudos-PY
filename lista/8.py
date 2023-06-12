def calculadora(num1, num2,simbolo):
    if simbolo == '+':
        print('a soma é: ', num1+num2)
    if simbolo == '-':
        print('a subtração é: ', num1-num2)
    if simbolo == '*':
        print('a multi é: ', num1*num2)
    if simbolo == '/':
        print('a divisão é: ', num1/num2)
        
num1 = int(input('Digite o 1 numero: '))
num2 = int(input('digite o 2 numero: '))
simbolo = input("Digite o simbolo da operação: ")
calculadora(num1, num2, simbolo)
        
    
    
    
    