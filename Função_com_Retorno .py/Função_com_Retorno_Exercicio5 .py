import os 
os.system("cls || clear")
from datetime import datetime
#def calcular_idade(ano_nascimento):
 #   return 2025 - ano_nascimento

def calcular_idade(ano_nascimento):
    return datetime.now().year - ano_nascimento

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = calcular_idade(ano_nascimento)

print(f"Idade: {idade}")