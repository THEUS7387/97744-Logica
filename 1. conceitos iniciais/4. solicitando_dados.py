import os

# Limpar o terminal.
os.system("clear")

#Solicitar dados do usuario.
nome = input ("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))


# Exibindo dados.
print()
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}")