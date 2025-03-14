import os 
import time
os.system("cls || clear")

numero = int(input("Digite um numero para contagem regressiva "))
print ("iniciando contagem regressiva: ")
for i in range(numero, 0, -1):
    print(f"{i}")
    time.sleep(1)

print("Acabou.")