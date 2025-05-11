# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do
# usuário e imprima a data com o nome do mês por extenso. O
# programa deve chamar uma função que retorna o mês convertido.
# Exemplo:
# – Entrada - Data de Nascimento: 29/10/1973
# – Saída - Você nasceu em 29 de Outubro de 1973.

def obter_mes_extenso(mes):
    meses = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }
    return meses.get(mes, "Mês inválido")


def formatar_data_nascimento(data):
    dia, mes, ano = data.split("/")
    mes_extenso = obter_mes_extenso(mes)
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
print(formatar_data_nascimento(data_nascimento))
