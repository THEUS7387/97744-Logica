import os 
#Limpando Terminall.
os.system("cls || clear")

#Laço de Repetição While.
QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))
        if nota < 0 or nota > 10:
            print("Nota Invalida, tente novamente.\n")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado."
elif media >= 5:
    resultado = "Recuperação."
else:
    resultado = "Reprovado."

print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")