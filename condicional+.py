#ATIVIDADE CLUBE DE FUTEBOL

print("Clube de Regatas do Flamengo/nCadastro de atleta")
idade = int(input("Digite sua idade: "))
if idade >= 5 and idade <= 10:
  print("Jogador do Infantil")
elif idade >= 11 and idade <= 15:
  print("Jogador do Juvenil")
elif idade >= 16 and idade <= 20:
  print("Jogador do Júnior")
elif idade >= 21 and idade <= 25:
  print("Jogador do Profissional")
else: 
  print("Opção Invalida")

#CODIGO DE ORIGEM
origem = int(input("Digite o codigo do produto: "))
if origem == 1 or origem == 2:
  print("Sul")
elif origem == 3 or origem == 4:
  print("Sudeste")
elif origem == 5 or origem == 6:
  print("Norte")
elif origem == 7 or origem == 8:
  print("Nordeste")
elif origem == 9 or origem == 10:
  print("Centro-Oeste")
else:
  print("FODA-SE")

#CODIGO PRODUTO COMIDAS
cdg = int(input("Digite o codigo: "))
if cdg == 1:
  print("Pizza")
elif cdg ==2:
  print("Hamburguer")
elif cdg ==3:
  print("Refri")
elif cdg ==4:
  print("Batata frita")
else:
  print("Foda-se")

#VASCO FLAMENGO
fla = int(input("Digite o numero de gols do flamengo: "))
vasco = int(input("Digite o numero de gols do vasco: "))
if fla == vasco:
  print("Empate")
elif fla > vasco:
  print("Flamengo ganhou")
else:
  print("Impossivel vasco ganhar!!!")



#CODIGO E OPERAÇÃO
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("1- Média\n2- Diferença\n3- produto\n4-Divisão")
op = int(input("Digite a opção desejada: "))
if op == 1:
  print("A media é: ", (num1 + num2)/2)
elif op == 2:
     
  if num1 > num2:
    print("A diferença é: ",num1 - num2)
  elif num2 > num1:
    print("A diferença é: ", num2 - num1)
    
elif op ==3 :
  print("O produto é: ", num1 * num2)
elif op == 4:
  print("A divisão é: ", num1 / num2)
else:
  print("Codigo invalido")

#PERCENTUAL AUMENTO

sal = float(input("Digite seu salario: "))
if sal < 300:
  print("Seu novo salario é: ", sal * 1.45)
elif sal >= 300 and sal <= 600:
  print("Seu novo salario é: ", sal * 1.25)
elif sal > 600:
  print("Seu novo salario é: ", sal *1.15)
else:
  print("Opção Invalida!!")


#ESOLHA DO USUARIO MAIOR MENOR
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
escolha = int(input("Digite sua opção: "))
if escolha == 1 or escolha == 2:
  if num1 > num2:
    print("Primeiro numero maior")
  else:
    print("Segundo numero maior")
elif escolha == 3 or escolha == 4:
    if num1 < num2 :
      print("Primeiro numero menor")
    else:
      print("Segundo numero menor")
else:
  print("erro de código")
  