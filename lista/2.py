def aprovado(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) /3
    if(media >= 7):
        print(f"Sua média é {media}, está aprovado")
    else:
        print(f"Sua média é {media}, está reprovado")
        

num1 = int(input('Digite a primeira nota: '))
num2 = int(input('Digite a segunda nota: '))
num3 = int(input('digite a terceira nota : '))
aprovado(num1, num2, num3)
