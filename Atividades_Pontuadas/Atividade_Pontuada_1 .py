import os 

#Limpando Terminal.
os.system("Clear")

A = float(input("Digite o Valor de A: "))
B = float(input("Digite o Valor de B: "))
C = float(input("Digite o Valor de C: ")) 

if A + B < C:
    print("A + B é menor que C")
else:
    print("A + B é maior ou igual a C")

