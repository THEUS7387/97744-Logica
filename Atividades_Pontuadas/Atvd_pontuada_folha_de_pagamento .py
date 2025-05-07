import os
os.system("Cls || clear")

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario >= 1518.01 and salario <= 2793.88:
        return salario * 0.09
    elif salario >= 2793.89 and salario <= 4190.83:
        return salario * 0.12
    elif salario >= 2793.89 and salario <= 8157.41:
        return salario * 0.14
    else:
        return 1142.04

def calcular_irrf(salario, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - deducao_dependentes

    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo >= 2259.21 and base_calculo <= 2826.65:
        return base_calculo * 0.075
    elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
        return base_calculo * 0.15
    elif base_calculo >= 3751.06 and base_calculo <= 4664.68:
        return base_calculo * 0.225
    else:
        return base_calculo * 0.275

def calcular_vale_transporte(salario, vt):
    return salario * 0.06 if vt.lower() == 's' else 0.0

def calcular_vale_refeicao(vr):
    return vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def main():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    print("Acesso autorizado!\n")
   
    salario_base = float(input("Digite o salário base do funcionário: "))
    vt = input("Deseja receber vale transporte? (s/n): ")
    vr = float(input("Digite o valor do vale refeição fornecido pela empresa: "))
    dependentes = int(input("Digite a quantidade de dependentes: "))

    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, dependentes)
    desconto_vt = calcular_vale_transporte(salario_base, vt)
    desconto_vr = calcular_vale_refeicao(vr)
    desconto_saude = calcular_plano_saude(dependentes)

    total_descontos = desconto_inss + desconto_irrf + desconto_vt + desconto_vr + desconto_saude
    salario_liquido = salario_base - total_descontos

    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

main()