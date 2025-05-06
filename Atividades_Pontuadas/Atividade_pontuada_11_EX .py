import os 
os.system("cls || clear")

# Funçao para calcular media. 
def calcular_media(lista):
    # sum(lista) ira somar os valores da lista.
    # len (lista) ira mostrar a quantidade de valores na lista.
    media = sum(lista) / len(lista)
    return media

lista_notas = [] # Criando uma lista.
QUANTIDADE_NOTAS = 2 # Criando uma constante.

# Solicitando dados para o usuario.
for i in range(QUANTIDADE_NOTAS):
    nota = float (input(f"Digite a {1+1}ª nota: "))
    lista_notas.append(nota)
# Chamando a função para calcular a media.
# Enviando a lista de notas como parametro.
# Inserindo na variavel "media" o calculo retornado pela fumção.
media = calcular_media(lista_notas)
# Exibindo a media.
print(f"Media; {media}")