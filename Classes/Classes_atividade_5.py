import os 
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str

autor1 = Autor(
    nome = input("Digite o nome do autor: "),
    biografia = (input("Digite a biografia do autor: "))
)

@dataclass
class Livro:
    titulo: str
    ano: int

livro1 = Livro(
    titulo = input("Digite o titulo do livro: "),
    ano = (input("Digite o ano de publicação do livro: "))
)

print()

print("Informe os dados do autor da obra")
print(f"Nome: {Autor.biografia} ")
print(f":Titulo: {Livro.titulo} ")
print()