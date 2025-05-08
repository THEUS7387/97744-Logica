import os
from dataclasses import dataclass

# Limpa o Terminal
os.system("cls || clear")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Aplicando caracteristicas da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Aplicando caracteristicas da classse Pet.
pet1 = Pet("Totó", 4, 7.8) 
pet2 = Pet("Tubarão", 6, 9.2)

print("\n= Dados da Pessoa =")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos. ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")

print("\n= Dados do Pet =")
print(f"Nome: {pet1.nome}, idade: {pet1.idade} anos, Peso: {pet1.peso} kilos. ")
print(f"Nome: {pet2.nome}, idade: {pet2.idade} anos, Peso: {pet2.peso} kilos. ")