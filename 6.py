medias = []
for x in range(10):
    num1 = int(input('Digite a 1 nota: '))
    num2 = int(input('Digite a 2 nota: '))
    num3 = int(input('Digite a 3 nota: '))
    num4 = int(input('Digite a 4 nota: '))
    soma = num1 + num2 + num3 + num4
    media = soma / 4
    medias.append(media)
    
contador = 0
for media in medias:
    if media >= 7:
        contador += 1
        
print(contador)