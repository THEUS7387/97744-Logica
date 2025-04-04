import os 
os.system("cls || clear")

def verificar(numero):
    if numero > 0:
        print("O Número é Positivo.")
    elif numero ==0:
        print("O Número é Neutro.")

    else:
        print("O Número Negativo.")

print("Verificando se um Número é Positivo ou Negativo.")
numero = int(input("Digite um Número: "))
verificar(numero) 
