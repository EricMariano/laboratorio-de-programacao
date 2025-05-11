#7 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0    A
# Entre 7.5 e 9.0     B
# Entre 6.0 e 7.5     C
# Entre 4.0 e 6.0     D
# Entre 4.0 e zero    E
# O algoritmo deve mostrar na tela as notas, a média, 
# o conceito correspondente e a mensagem “APROVADO” se
# o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def calcular_conceito(media):
    if 9 <= media <= 10:
        return 'A', 'Aprovado'
    elif 7.5 <= media < 9:
        return 'B', 'Aprovado'
    elif 6 <= media < 7.5:
        return 'C', 'Aprovado'
    elif 4 <= media < 6:
        return 'D', 'Reprovado'
    else:
        return 'E', 'Reprovado'
    
def main():
    nota1 = float(input('Digite sua primeira nota no semestre: '))
    nota2 = float(input('Digite sua segunda nota no semestre: '))
    media = (nota1 + nota2) / 2
    conceito, status = calcular_conceito(media)  

    print(f'Notas: {nota1 , nota2}')  
    print(f'Média: {media}')  
    print(f'Conceito: {conceito}')  
    print(f'Status: {status}')

if __name__ == '__main__':
    main() 