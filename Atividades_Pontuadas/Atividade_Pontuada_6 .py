import os 

#Limpando Terminal.
os.system("Clear")

# Solicitando ao Usuário que digite as duas notas.
nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: ")) 

# Calculando a média aritmética das notas.
media = (nota1 + nota2) / 2 

# Exibindo a média.

print(f"\nMédia do aluno: {media:.2f}") 

# Verificando a situação do aluno
if media >= 6.0: print("Parabéns! Você foi APROVADO! ") 

elif 4.0 <= media < 6.0: print("Atenção! Você está de RECUPERAÇÃO.") 

else:
     print("Infelizmente, Você foi REPROVADO. ")