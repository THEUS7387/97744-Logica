import os
os.system("cls || clear")
 #Criando uma Lista.
lista_de_numeros =[]
QUANTIDADE = 5

#solicitando Dados ao Usuario.
for i in range(QUANTIDADE):
    numero = int(input(f"Digite um numero para lista: "))
    lista_de_numeros.append(numero)

menor = min(lista_de_numeros)
maior = max(lista_de_numeros)

#Exibindo Numeros da Lista.
print("\n= NUMEROS DA LISTA =")
for numero in enumerate(lista_de_numeros, start=1):
    print(f"{i} {numero}")

print(f"Maior numero: {maior}")
print(f"Menor numero: {numero}")