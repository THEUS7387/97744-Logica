import os 
os.system("cls || clear")

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero_informado = int(input("Digite um numero para a tabuada: "))
tabuada(numero_informado)