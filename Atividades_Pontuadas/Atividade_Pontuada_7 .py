import os 

#Limpando Terminal.
os.system("Clear")

# Solicitando os dados do produto ao usuário.
produto = input("Digite a descrição do produto: ") 
quantidade = int(input("Digite a quantidade adquirida: ")) 
preco_unitario = float(input("Digite o preço unitário do produto: ")) 

#Calculando o total sem desconto.
total = quantidade * preco_unitario 

# Determinando o percentual de desconto conforme a quantidade.
if quantidade <= 5: desconto_percentual = 2 

elif quantidade <= 10: desconto_percentual = 3 


else:
    desconto_percentual = 5 

# Calculando o valor do desconto.
desconto = (desconto_percentual / 100) * total 

# Calculando o total a pagar após o desconto.
total_a_pagar = total - desconto 

# Exibindo os resultados. 
print("\n=== RESUMO DA COMPRA ===")
print(f"Produto: {produto}") 
print(f"Quantidade: {quantidade}") 
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Total: R$ {total:.2f}") 
print(f"Desconto ({desconto_percentual}%): R$ {desconto:.2f}") 
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")