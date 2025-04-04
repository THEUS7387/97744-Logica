import os
os.system("cls || clear")

def converter_centimetros(numero):
    return numero * 100

numero = float(input("Digite um valor em Metros: "))

centimetros = converter_centimetros(numero)

print(f"Convertendo {numero} metros em centimetros é: {centimetros}")