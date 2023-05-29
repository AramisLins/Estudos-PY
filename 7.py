perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?" ]

contadordeSim = 0

for pergunta in perguntas:
   resposta = input(pergunta).lower()
   if resposta == 's':
       contadordeSim += 1
       
if  contadordeSim == 2:
    print('suspeito')    
       
elif  contadordeSim == 3 or contadordeSim == 4:
    print('cumplice')    
           
elif contadordeSim == 5:
    print ('assassiinoo')

else:
    print('salvo pelo gongo')