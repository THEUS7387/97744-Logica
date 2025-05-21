import os 
from dataclasses import dataclass
os.system("clss || clear")

@dataclass 

class Funcionario:
    nome = str
    cpf = str
    cargo = str
    salario = float

funcionarios = []

def mostrar_menu():
    print("\n--| SEJA BEM VINDO A DÊNDE TECH |--")
    print("1- Cadastrar funcionario")
    print("2- Listar funcionário")
    print("3- Atulizar funcionário")
    print("4- Exlcuir funcionário")
    print("5- Salvar dados em CSV ")
    print("6, Carregar de CSV")
    print("7,Sair")
    print()

def cadastrar():
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    cargo = input("Cargo: ")
    salario = input("Salario: ")
    funcionarios = input("Funcionarios: ")
    print("Funcionario cadastrado!")

def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
for f in funcionarios:
    print(f"{f.nome} | CPF: {f.cpf} | Cargo: {f.cargo} | Salário: R${f.salario}")


def atualizar():
    cpf = input("Digite o CPF do funcionario: ")
    if f.cpf:
        f.nome = input("Novo nome: ")
        f.cargo = input("Novo cargo: ")
        f.cargo = input("Novo salario: ")
        print("Funcionario atualizado!")
        return
    print("Funcionario não encontrado.")

def deletar():
    cpf = input("Digite o CPF do funcionario: ")
    for f in funcionarios:
        if f.cpf == cpf:
            funcionarios.remove(f)
            print("Funcionario removido!")
            return
    print("Funcionario não encontrado.")

def salvar_csv():
    with open("funcionarios.csv", "w", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for f in funcionarios:
            escritor = csv.writerow({f.nome, f.cpf, f.cargo, f.salario})
        print("Dados salvos no arquivo 'funcionarios.csv'.")

def carregar_csv():
    try:
        with open("funciuonarios.csv, "r") as arquivo:
            leitor =