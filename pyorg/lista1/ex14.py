# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print('Fish Weight and Penalty detector!')

fishWeigth = float(input('Enter a fish weight: '))
penaltyFixedValue = 4
maxWeight = 50

if fishWeigth > maxWeight:
    penaltyValue = (fishWeigth - maxWeight) * penaltyFixedValue
    print(f'The penalty value is {penaltyValue:.2f}$')
else:
    print('There is no penalty for the fish weigth')

