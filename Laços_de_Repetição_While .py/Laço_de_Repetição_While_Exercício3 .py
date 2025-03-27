import os

os.system("cls || clear")

#Atividade com Laço de Repetição.
login_cadastrado = "Mateus"
senha_cadastrada = "1234"

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo!")
        break
    else:
        print("Acesso negado. \nTente novamente")
