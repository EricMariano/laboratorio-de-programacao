#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Digite o lado do quadrado em cm: '))
area = lado ** 2
area2 = area * 2

print(f'A área do quadrado dado é {area:.1f}cm e o seu dobro é de {area2}cm')

