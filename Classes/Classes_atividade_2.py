import os
os.system("cls || clear")

from dataclasses import dataclass
@dataclass
class Endereco:
    logradouro: str
    numero: int
@dataclass
class Pessoa:
    # Variaveis = Atribuidos
    nome: set
    idade: int 
    endereco: Endereco
# Funçao = Método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, numero: {self.endereco.numero}")
# Aplicando caracteristicas a classe.
endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta", 44, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B", 47)
pessoa2 = Pessoa("Marta", 44, endereco2)
pessoa2.exibir_dados()