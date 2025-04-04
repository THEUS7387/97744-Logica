import os
os.system("cls || clear")

#Função sem retorno.
#Definindo caracteristicas da função.
def saudacao(nome, nome_disciplina):
    print(f"Olá {nome}! Bem-vindo(a) ao curso de DS!")
    print(f"A disciplina {nome_disciplina} faz parte do curso de DS!")

nome = input("Digite seu nome: ")
nome_disciplina = input("Digite o nome da disciplina: ")

saudacao(nome, nome_disciplina) #Chamando a função.