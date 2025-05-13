import os 
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

livro1 = Livro(
    nome = input("digite o nome do livro: "),
    autor = str(input("digite o nome do autor: ")),
    categoria = str(input("digite o nome do categoria: ")),
    preco = float(input("digite o nome do preço: "))
)

print("Informe um Segundo livro.")

livro2 = Livro(
    nome = input("digite o nome do livro: "),
    autor = str(input("digite o nome do autor: ")),
    categoria = str(input("digite o nome do categoria: ")),
    preco = float(input("digite o nome do preço: "))
)
print("Informe um Terceiro livro.")

livro3 = Livro(
    nome = input("digite o nome do livro: "),
    autor = str(input("digite o nome do autor: ")),
    categoria = str(input("digite o nome do categoria: ")),
    preco = float(input("digite o nome do preço: "))
)

