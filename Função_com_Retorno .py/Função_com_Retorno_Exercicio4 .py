import os 
os.system("cls || clear")

def inflaciona(preco):
    if preco < 100:
        valor = preco * 1.10
    else:
        valor = preco * 1.20
    return valor

preco = float(input("Digite o Valor do Produto: "))

preco_final = inflaciona(preco)

print(f"Preço Final: {preco_final:.2f}")