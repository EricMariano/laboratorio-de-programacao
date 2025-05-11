#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('')
n1 = float(input('Enter yours first note: '))
n2 = float(input('Enter yours second note: '))
n3 = float(input('Enter yours third note: '))
n4 = float(input('Enter yours fourth note: '))

overallAvarage = (n1 + n2 + n3 + n4) / 4

print(f'Your average in first two months is  {overallAvarage:.1f}')