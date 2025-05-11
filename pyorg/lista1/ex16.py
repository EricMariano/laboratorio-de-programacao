# 16.Faça um programa para uma loja de tintas. O programa deverá pedir 
# o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe 
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# 1l pinta 3m² -> 18l pinta 54m -> um balde custa $80 print('qtdLatas e precoTotal')
metersForPaint = float(input('Enter the size of the area to be painted: '))
lata = metersForPaint / 54

if metersForPaint % 54 != 0:  
    lata = int(lata) + 1
else: 
    lata = int(lata)

price = lata * 80.00

print(f"The number of paint's cans required is {lata} and the price is ${price}")