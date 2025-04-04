import os
import time 
os.system("cls || clear")

def media(n1, n2):
    # Poderia ter sido assim tbm.
    # return (n1+ n2) / 2.
    calcular = (n1 + n2) / 2
    return calcular 

n1 = float(input("Digite o Primeiro Numero: "))
n2 = float(input("Digite o Segundo Numero: "))

time.sleep(1)
print("Calculando a Media Destes numeros...")
time.sleep(1)
Media = (n1 + n2) / 2
print(f"Resultado da Media: {Media:.2f}")