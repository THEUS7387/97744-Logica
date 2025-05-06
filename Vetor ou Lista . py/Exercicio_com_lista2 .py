import os
os.system("cls || clear")
 #Criando uma Lista.
lista_de_numeros =[]
QUANTIDADE = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 ==0:
            pares += 1
        else:
            impares += 1
    return pares, impares

#Solicitando dados para o usuario.
print("= LISTA DE NUMEROS =")
for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i+1}º numero:"))
    lista_de_numeros.append(numero)

pares, impares = pares_impares(lista_de_numeros)

#Exibindo numeros da lista
print("\= NUMEROS DA LISTA =")
for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"{i}: {numero}")

print(f"\nPares:{pares}")
print(f"Impares: {impares}")