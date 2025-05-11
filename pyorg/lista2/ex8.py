# 8. Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def verifica_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'
    
def main():
    lado1 = float(input('Digite o primeiro lado do triângulo: '))
    lado2 = float(input('Digite o segundo lado do triângulo: '))
    lado3 = float(input('Digite o terceiro lado do triângulo: '))

    if verifica_triangulo(lado1, lado2, lado3):
        print('Os lados formam um triângulo.')
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print(f"O triângulo é {tipo}.")
    else:
        print('Os lados não formam um triângulo.')

if __name__ == '__main__':
    main()