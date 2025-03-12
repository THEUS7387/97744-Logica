import os 

#Limpando Terminal.
os.system("Clear")

# Solicitando ao Usuário a cor do CD.
cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().lower() 

# Definindo os preços com base na cor informada.
match cor: 

    case "verde": 
        preco = 10.00 

    case "azul": 
        preco = 20.00 

    case "amarelo": 
        preco = 30.00 

    case "vermelho": 
        preco = 40.00 

    case _: 
        preco = None # Indica que a cor não é válida. 

# Exibe o preço correspondente ou mensagem de erro.
if preco is not None: 
    print(f"\nO preço do CD da cor {cor.capitalize()} é R$ {preco:.2f}") 

else: 
    print("\nCor inválida! Por favor, escolha entre Verde, Azul, Amarelo ou Vermelho.")