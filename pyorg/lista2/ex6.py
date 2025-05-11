#6 Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = input('Digite um número de 1 a 7 para escolher qual dia da semana deseja: ')

dias = {
    '1': 'Domingo',
    '2': 'Segunda-Feira',
    '3': 'Terça-Feira',
    '4': 'Quarta-Feira',
    '5': 'Quinta-Feira',
    '6': 'Sexta-Feira',
    '7': 'Sábado'
}

print(dias.get(numero, 'Valor Inválido!'))
