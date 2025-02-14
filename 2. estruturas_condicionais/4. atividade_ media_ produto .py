import os

primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2

if primeiro_numero < segundo_numero:
    maior_numero = segundo_numero 
    menor_numero = primeiro_numero

else:    
    maior_numero = segundo_numero 
    menor_numero = primeiro_numero

print()
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Media: {media}")

if primeiro_numero == segundo_numero:
    print(f"Os numeros sao iguais")

else:
    print(f"Maior numero: {maior_numero}")
    print(f"Menor numero: {menor_numero}")
