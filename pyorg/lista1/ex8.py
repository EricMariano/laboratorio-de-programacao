#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
dinhora = float(input('Informe quanto você ganha por hora: '))
horames = float(input('Informe quantas horas você trabalha por mês: '))
salario = dinhora * horames

print(f'Seu salário mês é de R${salario}')