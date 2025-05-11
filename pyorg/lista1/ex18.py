# 18.Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

# MB => megabytes | Mbps => megabits por segundos 
tamanhoArquivo = float(input('coloque o tamanho do arquivo em MB: '))
velocidadeLink = float(input('coloque a velocidade do link em Mbps: '))

velocidadeMBps = velocidadeLink / 8

tempoEmSegundos = tamanhoArquivo / velocidadeMBps

tempoEmMinutos = tempoEmSegundos / 60

print(f'O tempo de download do arquivo é de {tempoEmMinutos:.2f} minutos')
