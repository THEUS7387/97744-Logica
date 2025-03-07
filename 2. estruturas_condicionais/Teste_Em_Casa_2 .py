import os

#Limpando o Terminal.
os.system("clear")

#Solicitando o Valor do Produto.
valor_produto = float(input("Digite o Valor do Produto: "))
print("""         
====================FORMA DE PAGAMENTO===================="
"1 \tA vista
2 \tA prazo"
""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

# Verificando.
match forma_de_pagamento:
    case 1:
        #Obtendo o valor do desconto 10%.
        desconto = vaqlor_produto * 0.10
        valor_com_desconto = valor_produto - desconto

        #Exibindo Resultados.
         print(f"\nValor do produto: R$ {valor_do_produto}")
         print(f"Forma de pagamento: a vista")
         print(f"Valor do desconto: R${desconto}")
         print(f"Total a pagar: R$ {valor_com_desconto}")
         
    case 2:
         quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
         if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
             valor_da_parcela = valor_do_produto / quantidade_parcelas

             #Exibindo resultados.