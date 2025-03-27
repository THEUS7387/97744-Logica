import os

os.system("cls || clear")

login_cadastrado = "Mateus"
senha_cadastrada = "1234"
contador = 0

for i in range(3):
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo!")
        break
    else:
        print("Acesso negado. \nTente novamente")
        if i == 2:
            print ("Numero de tentativas acima do limite permitido.\n")