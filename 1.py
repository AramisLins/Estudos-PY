altura = [[0,0],[0,0]]
qtd = 0

for l in range(2):
    for c in range (2):
        altura[l][c] = float(input('Digite sua altura: '))
        if altura[l][c] > 1.5:
            qtd += 1

print(qtd)
        