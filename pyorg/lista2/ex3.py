# 3.Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# print('Em qual turno você estuda?')
# turno = input('M-matutino ou V-Vespertino ou N-Noturno: ')

# if turno.lower() == 'm' or turno.lower == 'matutino':
#     print('Bom dia!')
# elif turno.lower() == 'v' or turno.lower == 'vespertino':
#     print('Boa tarde!')
# elif turno.lower() == 'n' or turno.lower == 'noturno':
#     print('Boa noite!')
# else:
#     print('Valor Inválido!')

print('Em qual turno você estuda?')
turno = input('M-matutino ou V-Vespertino ou N-Noturno: ').lower()

saudacoes = {
    'm': 'Bom dia!',
    'matutino': 'Bom dia!',
    'v': 'Boa tarde!',
    'vespertino': 'Boa tarde!',
    'n': 'Boa noite!',
    'noturno': 'Boa noite!'
}

print(saudacoes.get(turno, 'Valor Inválido!'))