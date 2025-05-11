#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1int = float(input('Digite um número inteiro: '))
n2int = float(input('Digite outro número inteiro: '))
nreal = float(input('Agora, digite um número real: '))

a = (n1int * 2) + (n2int / 2)
b = (n1int * 3) + nreal
c = nreal **3

print(f'A = {a}, b = {b}, c = {c:.1f}')