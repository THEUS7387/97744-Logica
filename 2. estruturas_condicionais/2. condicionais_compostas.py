import os 

os.system("clear") # Limpa o terminal.

# Solicitando dados (Entrada)
idade = int(input("Digite sua idade"))

# Verificando (Processamento)
if idade < 18:
    print("Acesso negado!")

    # Exibindo dados (Saida)
    print("== Fim ==")
