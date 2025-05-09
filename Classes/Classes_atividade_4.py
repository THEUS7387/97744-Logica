import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = [] # Criando uma lista para adicionar clientes.
QUANTIDADE_CLIENTES = 2 # Constantes que define a quantidade de clientes.

# Laço de repetição para adicionar clientes.
print("Informe os dados do cliente: ")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente( # Instanciando um objeto.
        nome = input("Nome: "), # Não esqueça da vírgula.
        email = input("E-mail: "),
        telefone = input("Telefone: ")
)
lista_clientes.append(cliente) # Adicionando um cliente na lista.
print()

# Laço de repetição para exibir dados dos clientes.
print("\n= Exibindo dados dos clientes =")
for i in lista_clientes: # Mostra os dados por elementos na lista.
    print(f"Nome: {cliente.nome} ")
    print(f"E-mail: {cliente.email} ")
    print(f"Telefone: {cliente.telefone} ")
    print()

# Salvando em um arquivo .txt
print("= Salvando os dados dos clientes= ")
nome_arquivo = "dados_clientes.txt"

 # w -> escrita/salvar/sobrescrever
 # a -> escrita/salvar/acumular
with open(nome_arquivo, "w") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}\n")

print("\Salvo com sucesso!")