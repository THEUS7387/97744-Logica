import os

# Limpar o terminal.
os.system("clear")

# Solicitar os dados do usuário
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").strip().upper() 
estado_civil = input("Digite seu estado civil (Solteira/Casada/Divorciada/Viúva): ").strip().upper()

# Começar a variável tempo_casada.
tempo_casada = None 

# Se a pessoa for do sexo feminino e casada, solicitando o tempo de casamento.
if sexo == "F" and estado_civil == "CASADA":
     tempo_casada = input("Há quantos anos você está casada? ") 
   
     # Exibindo os dados.
     print("\n--- Dados da Pessoa ---") 
     print(f"Nome: {nome}")
     print(f"Sexo: {sexo}")
     print(f"Estado Civil: {estado_civil}") 
   
     # Exibibindo o tempo de casada se assim for.
     if tempo_casada is not None:
          print(f"Tempo de Casada: {tempo_casada} anos") 