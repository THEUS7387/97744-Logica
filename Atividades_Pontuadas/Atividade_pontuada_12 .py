import os
os.system("Cls || clear")

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04  # Teto de contribuição

def calcular_irrf(salario_base, inss, dependentes):
    base_calculo = salario_base - inss - (dependentes * 189.59)

    if base_calculo <= 2259.20:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_salario_liquido():
    print("=== CÁLCULO DE FOLHA DE PAGAMENTO ===")

    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    salario_base = float(input("Digite o salário base (R$): "))
    vt_opcao = input("Deseja receber vale transporte? (s/n): ").strip().lower()
    vale_transporte = vt_opcao == 's'
    valor_vale_refeicao = float(input("Digite o valor do vale refeição (R$): "))
    dependentes = int(input("Digite a quantidade de dependentes: "))

    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, desconto_inss, dependentes)
    desconto_vale_transporte = salario_base * 0.06 if vale_transporte else 0
    desconto_vale_refeicao = valor_vale_refeicao * 0.20
    desconto_plano_saude = dependentes * 150.00

    total_descontos = (
        desconto_inss +
        desconto_irrf +
        desconto_vale_transporte +
        desconto_vale_refeicao +
        desconto_plano_saude
    )

    salario_liquido = salario_base - total_descontos

    print("\n--- FOLHA DE PAGAMENTO ---")
    print(f"Matrícula: {matricula}")
    print(f"Salário base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

# Executar o sistema
calcular_salario_liquido()
