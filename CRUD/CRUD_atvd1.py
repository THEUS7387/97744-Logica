import os 
from dataclasses import dataclass
os.system("clas || clear")

@dataclass
class Funcionario:
    nome = str
    data_nascimento = int
    cpf = int
    funcao = str
def __init__(self, nome, data_nascimento, cpf, funcao):
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf
    self.funcao = funcao

def __str__(self):
    return f"Nome: {self.nome}, {self.data_nascimento}, {self.cpf}, {self.funcao}"

funcionario = []
def criar():
    print("\n--- Casdastrar ---")
    funcionario.append(funcionario(input("Nome: "), input("Data de Nascimento: "), input("CPF: "), input("Função: ")))
    print("Cadastrado com sucesso!")

def ler():
    print("\n--- Lista ---")
    [print(funcionario) for i in funcionario] if funcionario else print("\nSem cadastros.")


def atualizar():
    if not funcionario: print("\nSem cadastros."); return
    cpf_funcionario = input("\nCPF para atualizar: ")
    for funcionario in funcionario:
        if funcionario.cpf == cpf_funcionario:
            print(f"\n--- Atualizar: {funcionario.nome} ---")
            funcionario.nome = input(f"Novo nome: ({funcionario.nome}): ") or funcionario.nome
            funcionario.data_nascimento = input(f"Nova Data: ({funcionario.data_nascimento}): ") or funcionario.data_nascimento
            funcionario.cpf = input(f"Novo CPF: ({funcionario.cpf}): ") or funcionario.cpf
            funcionario.funcao = input(f"Nova Função: ({funcionario.funcao}): ") or funcionario.funcao
            print("Atualiazado com sucesso!.")
            return
    print("CPF não encontrado.")

def deletar():
    if not funcionarios: print("\nSem cadatros."); return
    cpf_deletar = ("\nCPF para deletar: ")
    for i, funcionario in enumerate(funcionarios):
        if funcionario.cpf == cpf_deletar:
            del funcionarios[i]
            print("Deletado com sucesso!.")
            return
        print("CPF encontrado.")

o = {"1": criar, "2": ler, "3": atualizar, "4": deletar, "5": exit}

while True:
    print("\n---Menu ---")
    [print(f"{k}. {v.__name__.upper()}") for k, v in o.items()]
    op = input("Opção: ")
    if op in o: o [op]()
    else: print("Invalido.")

