# 15.Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:

# salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido.

# calcule os descontos e o salário líquido Obs.: Salário Bruto - Descontos = Salário Líquido.

salPerHour = float(input('How much do you earn per hour? '))
hourWorkedMon = float(input('How many hours do you work per month? '))

salaryTotal = salPerHour * hourWorkedMon

ir = 11/100
inss = 8/100
sind = 5/100

payIr = salaryTotal * ir
payInss = salaryTotal * inss
paySind = salaryTotal * sind

discountTotal = payInss + payIr + paySind

salary = salaryTotal - discountTotal

print(f'You receive ${salaryTotal}, pay to INSS ${payInss} and  ${paySind} for sindicate. Your liquid salary is ${salary}')