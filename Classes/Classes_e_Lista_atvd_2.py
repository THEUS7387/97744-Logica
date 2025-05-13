import os 
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: str


@dataclass
class Cliente:
    nome: str
    data_nascimento: int
    endereco: str

nomeF1 = input("Nome")

