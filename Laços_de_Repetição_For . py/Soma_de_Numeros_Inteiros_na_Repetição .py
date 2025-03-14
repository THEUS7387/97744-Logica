import os

#Linpando Terminal. 
os.system("cls || clear")

soma = 0

for i in range (1, 6):
    numero = int(input("Digite um numero: "))
    # soma = soma + numero
    soma += numero
    print(F"Soma: {soma}")