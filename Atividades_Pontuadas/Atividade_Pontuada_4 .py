import os

#Limpando terminal.
os.system("clear")

# Solicitando ao Usuario a quantidade de morangos e maçãs em (Kg).
kg_morango = float(input("Digite a quantidade de Morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de Maçãs (Kg): "))

# Preços por Kg com base na quantidade comprada.  
if kg_morango <= 5:
    preco_morango = 2.50

else:
    preco_morango = 2.20


if kg_maca <= 5:
    preco_maca = 1.80

else:
    preco_maca = 1.50

# Calculando o valor total da compra.
valor_morango = kg_morango * preco_morango 
valor_maca = kg_maca * preco_maca
valor_total = valor_morango + valor_maca


# calculando se o cliente tem direito a 10% de desconto.
peso_total = kg_morango + kg_maca
if peso_total > 8 or valor_total > 50: 
    desconto = valor_total * 0.10 
    valor_total -= desconto


# Exibe o valor final da compra.
print(f"\nValor a se pago: R$ {valor_total: .2f}")
