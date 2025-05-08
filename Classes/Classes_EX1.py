import os 

from dataclasses import dataclass

# Limpa o Terminal
os.system("cls || clear")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

# Aplicando caracteristicas da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos. ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")