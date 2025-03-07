# Limpando Terminal
import os

os.system("clear")

#Solicitando Dados ao Usuario.
valor_produto = float(input("Digite o valor do produto: "))
print("""
      ======================== FORMA DE PAGAMENTO =======================
      1  \t A vista 
      2  \t A prazo
      """)
    forma_de_pagamento = int(input("Digite a forma de pagamento: "))

# Verificando.
match forma_de_pagamento:
    case 1:
# Obtendo o Valor do o Desconto de 15%0.
       Desconto = 100 * 0.10

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas: ")) 
        
    case _:
        print("Opcao invalida.")

# Exibindo Resultados.

print(100,00)
