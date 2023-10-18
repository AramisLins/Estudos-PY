#tkinter biblioteca gráfica
import tkinter as tk

#themed tkinter, é um conjunto de widgets
from tkinter import ttk
fonte = ("Arial", 10)

def exibir_mensagem():
    nome = nome_entry.get()
    idade = idade_entry.get()
    peso = peso_entry.get()
    mensagem_label["text"] = "Olá, " + nome +"de idade " + idade + "\nde peso " + peso
  



#criando a janela principal
root = tk.Tk()
root.title("Inova teste")


#cria o widgets
nome_label = ttk.Label(root, text="Nome: ", font=fonte)
nome_entry = ttk.Entry(root, font=fonte, width=30)

idade_label = ttk.Label(root, text="Idade: ", font=fonte)
idade_entry = ttk.Entry(root, font=fonte, width=30)

peso_label = ttk.Label(root, text="Peso: ", font=fonte)
peso_entry = ttk.Entry(root, font=fonte, width=30)

altura_label = ttk.Label(root, text="Altura: ", font=fonte)
altura_entry = ttk.Entry(root, font=fonte, width=30)













botao = ttk.Button(root, text="Clique aqui", command=exibir_mensagem)
mensagem_label = ttk.Label(root, text="", font=fonte)



#ajusta a posição na tela
nome_label.grid(row=0, column=0, padx=15, pady=10)
nome_entry.grid(row=0, column=1, padx=0, pady=15)
idade_label.grid(row=1, column=0, padx=15, pady=10)
idade_entry.grid(row=1, column=1, padx=15, pady=10)
peso_label.grid(row=2, column=0, padx=15, pady=10)
peso_entry.grid(row=2, column=1, padx=15, pady=10)
altura_label.grid(row=3, column=0, padx=15, pady=10)
altura_entry.grid(row=3, column=1, padx=15, pady=10)








botao.grid(row=3, column=0,columnspan=2, padx=5, pady=0)
mensagem_label.grid(row=4, column=0, columnspan=2, pady=5)

#inicia a interface gráfica
root.mainloop()


