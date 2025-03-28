import os 
 
familias = []
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = float('inf') 
def adicionar_familia():
    global soma_salarios, soma_filhos, maior_salario, menor_salario 
    print("\n--- Adicionar Família ---") 
    
    try:
         salario = float(input("Digite o salário da família: R$ "))
         num_filhos = int(input("Digite o número de filhos: ")) 
         
         if salario < 0 or num_filhos < 0:
             print("Erro: Valores não podem ser negativos!") 
             return
         familias.append((salario, num_filhos))
         soma_salarios += salario
         soma_filhos += num_filhos 
    
    if salario > maior_salario:
        maior_salario = salario 
    if salario < menor_salario:
        menor_salario = salario

        print("\nFamília adicionada com sucesso!") 

    except ValueError:

print("Erro: Por favor, insira valores numéricos válidos.")

def exibir_resultados(): 
    if not familias:
        print("\nNenhum dado registrado ainda.") 
        return 
    media_salarial = soma_salarios / len(familias) 
    if familias else 0 
    media_filhos = soma_filhos / len(familias) 
    if familias else 0 print("\n--- Resultados da Pesquisa ---") 
   
    print(f"A) Total de famílias que responderam: {len(familias)}")
    print(f"B) Média salarial da população: R$ {media_salarial:.2f}")
    print(f"C) Média do número de filhos: {media_filhos:.2f}")
    print(f"D) Maior salário registrado: R$ {maior_salario:.2f}") 
    print(f"E) Menor salário registrado: R$ {menor_salario:.2f}") 

def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    while True:
        print("\n--- MENU ---") 
        print("1 | Adicionar família")
        print("2 | Sair e exibir resultados")
