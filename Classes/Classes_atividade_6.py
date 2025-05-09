import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Carro:
    marca = str
    modelo = str
    categoria = str
    preco = float

carro1 = Carro(
    marca = input("Digite o nome da marca do carro: "),
    modelo = str (input("Digite o modelo do carro: ")),
    categoria = str (input("Digite a categoria do carro: ")),
    preco = float (input("Digite o preço do carro: "))
)
    

print("informe um segundo veiculo")

carro2 = Carro(
    marca = input("Digite o nome da marca do carro: "),
    modelo = str (input("Digite o modelo do carro: ")),
    categoria = str (input("Digite a categoria do carro: ")),
    preco = float (input("Digite o preço do carro: "))
)

print()

print("\n=DADOS DOS VEICULOS= ")
print(f"Marca: {carro1.marca}, Modelo: {carro1.modelo} categoria: {carro1.categoria} Preço: {carro1.preco} ")
print(f"Marca: {carro2.marca}, Modelo: {carro2.modelo} categoria: {carro2.categoria} Preço: {carro2.preco} ")