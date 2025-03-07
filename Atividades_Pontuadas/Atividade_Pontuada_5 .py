import os 

# Limpando o terminal
os.system("Clear")

# Solicitando a operação e os valores A e B
operacao = input("Digite a operação (+, -, *, /): ") 

A = int(input("Digite o valor de A: ")) 
B = int(input("Digite o valor de B: ")) 

# Dicionário de operações.
operacoes = { "+": A + B, 
             "-": A - B, 
             "*": A * B, 
             "/": A / B if B != 0 else "Erro! Divisão por zero." } 

# Calculando e exibindo o resultado.
resultado = operacoes.get(operacao, "Operação inválida!") 
print(f"\nO resultado é: {resultado}")