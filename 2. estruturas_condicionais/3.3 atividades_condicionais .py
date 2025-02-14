import os 

os.system("clear")

  nota_1 = float(input("digite 1 nota : "))
  nota_2 = float(input("digite 2 nota : ")) 
  nota_3 = float(input("digite 3 nota : "))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 7:
  resultado = "Reprovado!"

else: 
  resultado = "Aprovado!"

  print(f"\Media: {media}")
  print (f"Resultado: {resultado}") 