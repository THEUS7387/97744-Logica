import os 

#Limpando Terminal
os.system("Clear")

# Solicita os dados do solicitante
renda_mensal = float(input("Digite sua renda mensal: R$ ")) 
valor_emprestimo = float(input("Digite o valor total do empréstimo desejado: R$ ")) 
num_prestacoes = int(input("Digite o número de prestações: ")) 

# Calcula os critérios da financeira 
limite_emprestimo = renda_mensal * 10

# O empréstimo pode ser no máximo 10 vezes a renda 
valor_prestacao = valor_emprestimo / num_prestacoes 
# Valor de cada parcela 
limite_prestacao = renda_mensal * 0.30 #A parcela pode ser no máximo 30% da renda 

# Verifica se o empréstimo pode ser concedido 
if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao: 
    print("\nEmpréstimo APROVADO! ✅") 
    print(f"Valor da prestação: R$ {valor_prestacao:.2f}") 
else: 
    print("\nEmpréstimo NEGADO! ❌") 
    print("Motivos possíveis:") 
if valor_emprestimo > limite_emprestimo: 
    print(f"- O valor do empréstimo excede o limite permitido (máximo: R$ {limite_emprestimo:.2f})")
if valor_prestacao > limite_prestacao:
    print(f"- O valor da prestaçao execede 30% da sua renda mensal (máximo: R$ {limite_prestacao:.2f})")    