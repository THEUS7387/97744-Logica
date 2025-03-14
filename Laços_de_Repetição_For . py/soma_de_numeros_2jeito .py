import os 
#Limpando Terminal.
os.system("cls || clear")

numero = 0

for i in range(1, 6):
    numero += int (input("Digite um numero: "))
    print(f"soma: {numero}")