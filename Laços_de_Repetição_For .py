import os

#Limpando Terminal.
os.system("cls || clear")

print ("ímpares de 1 até 20:")
for i in range(1, 21):
    if i % 2 == 1:
        print(f"Núméro: {i}")