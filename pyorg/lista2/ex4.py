#4 Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
# seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def calcular_reajuste(salario):
    if salario <= 280:
        return 20
    elif salario <= 700:
        return 15
    elif salario <= 1500:
        return 10
    else:
        return 5
    
def exibir_informacoes(salario, percentual):
    valor_aumento = salario * percentual / 100
    novo_salario = salario + valor_aumento
    print(f'Salário antes do reajuste: R$ {salario:.2f}')
    print(f'Percentual de aumento aplicado: {percentual}%')
    print(f'Valor do aumento: R$ {valor_aumento:.2f}')
    print(f'Novo salário, após o aumento: R$ {novo_salario:.2f}')

def main():
    salario_atual = float(input('Digite o salário do colaborador: '))
    percentual_aumento = calcular_reajuste(salario_atual)
    exibir_informacoes(salario_atual, percentual_aumento)

if __name__ == "__main__":
    main()