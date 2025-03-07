import os
#Limpando o terminal. 
os.system

# Solicitando os valores inteiros A e B ao usuário.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
# Verificando se os valores são iguais ou diferentes e realizando o cálculo correspondente.
if A == B: C = A + B 

# Somando se forem iguais.
else: C = A * B

# Multiplicando se forem diferentes.
# Exibindo resultado.
print(f"\nO resultado do cálculo é: {C}")