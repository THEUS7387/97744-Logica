import os 
import time
os.system("cls || clear")

contador = 0 
soma_salario = 0
maior_idade = 0 
menor_idade = 9999 
mulheres5k = 0

while True:
    print(""""
Código | Descrição ""
       | Adicionar pessoa"
       | Exibir resultados"
       | Sair
""")
    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            idade = int(input("Informe sua Idade: "))
            sexo = input("Informe o sexo com 'M' ou 'F': ").upper()
            salario = float(input("Informe o salario: "))
            contador += 1
            soma_salario += salario

            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            os.system("cls || clear")
        case 2:
            if contador > 0:
                media_salario_grupo = soma_salario / contador
                print("\n= Exibindo resultados = ")
                print(f"Media de salario do grupo: {media_salario_grupo}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de Mulheres com salario a partir de 5 Mil: {mulheres5k}")
                time.sleep(3)
                os.system("cls || clear")
        case 3:
            break