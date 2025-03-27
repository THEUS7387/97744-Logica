import os 

os.system("cls || clear")

# Exemplo de uso de Laço de Repetição While.
while True:
    nota1 = float(input("Digite sua nota: "))

    if nota1 < 0 or nota1 > 10:
        print("Nota Invalida, tente novamente.\n")
    else:
        break

while True:
    nota2 = float(input("Digite a sua segunda nota: "))
    if nota2 < 0 or nota2 > 10:
        print("Nota Invalida, tente novamente.\n")
    else:
        break

media = (nota1 + nota2) / 2

print(f"Media: {media}")