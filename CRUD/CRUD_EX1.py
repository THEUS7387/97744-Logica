import os
import time

os.system("cls || clear")

nomes = [] #Criando lista de nomes.

#Menu.
while True:
    print("= Gerenciador de nomes =")
    print("1 - Adicionar")
    print("2 - Lista nomes")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpçaõ invalida. \nTente novamente.")
    if opcao != 1:
        time.sleep(5)
    os.system("cls || clear")