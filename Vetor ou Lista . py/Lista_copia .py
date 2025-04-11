import os 
os.system("cls || clear")

# Criando uma lista.
lista_de_compras = []
QUANTIDADE = 3

# Solicitando dados para o usuario.
print("_ LISTA DE COMPRAS _")
for i in range(QUANTIDADE):
    item = input(f"Digite o {i+1}º item para lista: ")
    lista_de_compras.append(item)

# Exibindo itens da lista de compras.
print("\n= ITENS DA LISTA =")
for item in enumerate(lista_de_compras, start=1):
    print(f"{i}º item: {item}")