import os
os.system("cls || clear")

def verificar(numero):
    if numero % 2 == 0:
        print("O Número é Par.")
    else:
        print("O Número é Impar")

print("Verificando se um Número é Par ou Impar.")
numero = int(input("Digite um Número: "))
verificar(numero) 
