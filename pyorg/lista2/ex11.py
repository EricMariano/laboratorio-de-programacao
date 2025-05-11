# 11. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# posso pegar o dia, mês e ano e verificar se eles são válidos, separando os indices do input e verificando 
# se o dia é menor que 31, o mês menor que 12 e o ano maior que 0.


def verificar_dia(dia):
    if dia < 1 or dia > 31:
        return False
    else:
        return True

def verificar_mes(mes):
    if mes < 1 or mes > 12:
        return False
    else:
        return True

def verificar_ano(ano):
    if ano < 0:
        return False
    else:
        return True

def verifica_ano_bissexto(ano):
    if ano % 4 == 0 :
        return True
    else: 
        print(f'{ano} não é um ano bissexto')
        return False

def verifica_fevereiro(mes, dia, ano):
    if mes == 2:
        if verifica_ano_bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    return True  

def verifica_dia_trinta(mes, dia):
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    else:
        return True
   
def main():
    while True:    
        print("=~=Verificador De Data=~=")
        
        data = input('Digite uma data no formato dd/mm/aaaa: ')

        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        if not verificar_dia(dia):
            print("Dia Inválido, Insira uma data válida.")
            continue
        elif not verificar_mes(mes):
            print("Mês Inválido, Insira uma data válida.")
            continue
        elif not verificar_ano(ano):
            print("Ano Inválido, Insira uma data válida.")
            continue
        elif not verifica_fevereiro(mes, dia, ano):
            print("Dia Inválido, Insira uma data válida.")
            continue
        elif not verifica_dia_trinta(mes, dia):
            print("Dia Inválido, Insira uma data válida.")
            continue
        else:
            print(f"A data, {data}, é válida")
            break


if __name__ == '__main__':
    main()