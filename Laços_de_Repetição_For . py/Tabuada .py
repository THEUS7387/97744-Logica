import os 

#Limpando Terminal.
os.system("cls || clear")

numero= int(input("Digite um numero para tabuada: "))

print(f"\nTabuada do numero {numero}:")
for i in range (1,11):
    print(f"{numero} x {i} = {i*numero}")