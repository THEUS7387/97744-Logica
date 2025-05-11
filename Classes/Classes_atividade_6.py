import os
os.system("cls || clear")
import time
from dataclasses import dataclass

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float

print("Informe o primeiro carro: ")

carro1 = Carro(
    marca = input("Digite o nome da marca do carro: "),
    modelo = str (input("Digite o modelo do carro: ")),
    categoria = str (input("Digite a categoria do carro: ")),
    preco = float (input("Digite o preço do carro: "))
)
    
time.sleep(1.05)

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

print("Vc possui um otimo gosto.")

# Salvando em um arquivo .txt
print("= Salvando os dados dos carros = ")
nome_arquivo = "dados_carros.txt"

 # w -> escrita/salvar/sobrescrever
 # a -> escrita/salvar/acumular
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("=DADOS DOS VEICULOS=\n")
    arquivo.write(f"Carro 1 - Marca: {carro1.marca}, Modelo: {carro1.modelo}, Categoria: {carro1.categoria}, Preço: {carro1.preco:.2f}\n")
    arquivo.write(f"Carro 2 - Marca: {carro2.marca}, Modelo: {carro2.modelo}, Categoria: {carro2.categoria}, Preço: {carro2.preco:.2f}\n")

print(f"\nOs dados dos veículos foram salvos no arquivo '{nome_arquivo}'.")