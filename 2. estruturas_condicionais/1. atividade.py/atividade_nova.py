# 1 - Limpando Terminal.
import os

os.system("clear")

# 2 - Solicitando Dados ao Usuario.

numero_mes = int(intup("Digite um numero de 1 a 12 para ver o mes correspondente: "))

match numero_mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")        
    case 3:
        print("Marco")
    case 4:
        print("abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")    
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")    
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")    
                    
    case _:
        print("Numero invalido! Digite um numero entre 1 a 12 para ver o correspondente:")            