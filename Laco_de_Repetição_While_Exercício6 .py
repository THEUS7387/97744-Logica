import os 

os.system("cls || clear")

# Inicializa as listas e variáveis para armazenar os dados
habitantes = [] 
soma_salarios = 0 
maior_idade = 0 
menor_idade = float('inf') # Define um valor muito alto para comparar
mulheres_acima_5000 = 0

def adicionar_pessoa():

    global soma_salarios, maior_idade, menor_idade, mulheres_acima_5000 
    
    print("\n--- Adicionar Pessoa ---") 
    
    try:
        idade = int(input("Digite a idade: ")) 
        sexo = input("Digite o sexo (M/F): ").strip().upper() 
        salario = float(input("Digite o salário: R$ ")) 

        if sexo not in ('M', 'F'): 
            print("Erro: Sexo inválido! Use 'M' para masculino e 'F' para feminino.") 
            return 
# Adiciona os dados à lista 
        habitantes.append((idade, sexo, salario))
        soma_salarios += salario 
    
# Atualiza maior e menor idade
        if idade > maior_idade:
            maior_idade = idade 
        if idade < menor_idade:
            menor_idade = idade 
# Conta mulheres com salário >= 5000
        if sexo == 'F' and salario >= 5000:
            mulheres_acima_5000 += 1 
            
            print("\nPessoa adicionada com sucesso!") 
    
    except ValueError:
         print("Erro: Por favor, insira valores válidos.")

def exibir_resultados(): 
    if not habitantes:
        print("\nNenhum dado registrado ainda.") 
        return
    media_salarial = soma_salarios / len(habitantes) if habitantes else 0
    print("\n--- Resultados da Pesquisa ---")
    print(f"A) Média salarial do grupo: R$ {media_salarial:.2f}")
    print(f"B) Maior idade: {maior_idade} anos")
    print(f" Menor idade: {menor_idade} anos")
    print(f"C) Mulheres com salário ≥ R$ 5.000,00: {mulheres_acima_5000}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela no Windows/Linux/Mac
# Loop principal do menu 

while True: 
    print("\n--- MENU ---") 
    print("1 | Adicionar pessoa") 
    print("2 | Exibir reultados") 
    print("3 | Sair")
    
    opcao = input("Escolha uma opção: ") 
    
    if opcao == '1':
        limpar_tela()
        adicionar_pessoa()
        
    elif opcao == '2':
        limpar_tela()
        exibir_resultados() 
    elif opcao == '3': print("\nPrograma encerrado. Obrigado!") 
    break 
else: 
    print("\nOpção inválida! Tente novamente.")