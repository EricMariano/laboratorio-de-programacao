import random

numeros_cartela_aleatoria = []
numeros_cartela = []

numeros_cartela_aleatoria = random.sample(range(1, 61), 6)
numeros_cartela.append(sorted(numeros_cartela_aleatoria))

print(f"Os números sorteados da MegaSena foram:\n {numeros_cartela}")