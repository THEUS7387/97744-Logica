import os 

#Limpando Terminal
os.system("Clear")

# Definição dos preços dos combustíveis.
preco_alcool = 3.79 
preco_gasolina = 6.59

# Solicitando ao usuário o tipo de combustível e a quantidade de litros.
tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").strip().upper() 
litros = float(input("Digite a quantidade de litros vendidos: "))

# Verificando o tipo de combustível e aplicando o desconto correspondente.
if tipo_combustivel == "A":
    preco_por_litro = preco_alcool 
    desconto = 0.02 if litros <= 25 else 0.04 # 2% até 25L, 4% acima.
elif tipo_combustivel == "G":
    preco_por_litro = preco_gasolina 
    desconto = 0.03 if litros <= 25 else 0.05 # 3% até 25L, 5% acima.
   
else:
    print("\nTipo de combustível inválido! Use 'A' para Álcool ou 'G' para Gasolina.") 
    exit() # Encerrando o programa caso a entrada seja inválida.
    
# Calculando o valor total sem desconto.
valor_total = litros * preco_por_litro
    
# Aplicando o desconto.
valor_desconto = valor_total * desconto 
valor_final = valor_total - valor_desconto
    
# Exibindo o resultado.
print("\n--- RESUMO DA COMPRA ---") 
print(f"Tipo de combustível: {'Álcool' if tipo_combustivel == 'A' else 'Gasolina'}") 
print(f"Quantidade de litros: {litros:.2f} L") 
print(f"Preço por litro: R$ {preco_por_litro:.2f}") 
print(f"Desconto aplicado: {desconto * 100:.0f}%") 
print(f"Valor do desconto: R$ {valor_desconto:.2f}") 
print(f"Total a pagar: R$ {valor_final:.2f}")