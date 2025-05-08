import os 
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(
    nome = input("Digite o seu nome: "),
    idade = int(input("Digite a sua idade: ")),
    peso = float(input("Digite o seu peso: ")),
    altura = float(input("Digite a sua altura: "))
    )

print()

pessoa2 = Pessoa(
    nome = input("Digite o seu nome: "),
    idade = int(input("Digite a sua idade: ")),
    peso = float(input("Digite o seu peso: ")),
    altura = float(input("Digite a sua altura: "))
    )

print()

print("\n=DADOS DA PESSOA = ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos. ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")