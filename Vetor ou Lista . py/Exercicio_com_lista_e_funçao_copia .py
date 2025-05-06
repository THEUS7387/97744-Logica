import os
os.system("cls || clear")

lista_de_numeros =[]
QUANTIDADE = 5

def maior_menor(lista):
    menor = min(lista)
    maior = max(lista)
    return menor, maior

def solicitar_dados():
    print("= NUMEROS DA LISTA =")
    for i in range(QUANTIDADE):
        numero = int(input("Digite um numero para a lista:"))
        lista_de_numeros.append(numero)


def mostrar_dados():
# Exibindo numeros da lista
    print("\n= NUMEROS DA LISTA =")
    for i, numero in enumerate(lista_de_numeros, start=1):
        print(f"{i}: {numero}")

    print(f"Maior numero: {maior}")
    print(f"Menor numero: {menor}")

#Chamando funções
solicitar_dados()
menor, maior = maior_menor(lista_de_numeros)
mostrar_dados()