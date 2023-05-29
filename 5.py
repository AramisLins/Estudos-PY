senhas = [['',''],['','']]

for l in range(2):
    for c in range(2):
        senhas[l][c] = input("Digite o banco de senha: ").lower()

verificacao = input('Qual a sua senha? ').lower()
senha_correta = False

for linha in senhas:
    for coluna in linha:
        if verificacao == coluna:
            senha_correta = True
            break

if senha_correta:
    print("Bem-Vindo!")
else:
    print("Usuário não Cadastrado!")
    
    
    