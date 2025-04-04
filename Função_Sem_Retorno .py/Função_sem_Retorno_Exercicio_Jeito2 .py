import os
os.system("cls || clear")
def saudacao(nome):
    print(f"Olá {nome}! Bem-vindo(a) ao curso de DS!")

def disciplina(nome):
    print(f"A Disciplina {nome} faz parte do curso de DS!")

nome = input("Digite seu nome: ")
nome_disciplina = input("Digite o nome da Disciplina: ")

saudacao(nome) #Chamando a função.
disciplina(nome_disciplina) #Chamando a função.