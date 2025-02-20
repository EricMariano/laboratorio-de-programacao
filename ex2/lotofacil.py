# a) Solicitar ao usuário a quantidade de dezenas que ele deseja marcar na primeira aposta (entre 15 e 18 números).
# Caso o usuário informe uma quantidade de dezenas fora do intervalo válido, o programa deve solicitar nova digitação,
# tantas vezes quantas forem necessárias;
# b) Solicitar ao usuário informar os números da primeira aposta (dezenas de 01 a 25, sem repetição). Caso o usuário
# informe um número repetido, o programa deverá apresentar uma mensagem “Número repetido” e solicitar nova
# digitação. Assim como se o usuário informar um número fora do intervalo válido, o programa deverá apresentar uma
# mensagem “Dezena inválida” e solicitar nova digitação.-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# c) Gerar aleatoriamente duas apostas, com 18 números, usando a “Surpresinha”. -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil; -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# e) Imprimir (em ordem crescente) as dezenas da primeira aposta, das duas apostas (surpresinha) e do resultado do
# concurso da Lotofácil simulado. -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from dataclasses import dataclass
import random

@dataclass
class FormularioLoteria:
    numero_dezena = 0
    numeros_universo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    numeros_cartela = []

    def quantidade_dezena(self):
        while True:
            try:
                self.numero_dezena = int(input("Quantas dezenas você quer marcar (entre 15 a 18 números): "))
                if 15 <= self.numero_dezena <= 18:
                    return
                print("Por favor, digite um número entre 15 e 18.")
            except ValueError:
                print("Digite apenas números.")


    def validar_cartela(self):
        print("\nEscolha 15 números diferentes")
        while len(self.numeros_cartela) < self.numero_dezena:
            try:
                numero_escolhido = int(input("\nDigite um número entre 1 e 25: "))
                if numero_escolhido < 1 or numero_escolhido > 25:
                    print("Dezena inválida! Digite um número entre 1 e 25.")
                    continue
                if numero_escolhido in self.numeros_cartela:
                    print("Número repetido! Escolha outro número.")
                    continue
                self.numeros_cartela.append(numero_escolhido)
            except ValueError:
                print("Digite apenas números.")

        print(sorted(self.numeros_cartela))        


    def resultado_loteria(self):   
        print("\nRESULTADO LOTOFACIL")
        sorteio_lotofacil = random.sample(self.numeros_universo, self.numero_dezena)
        print(f"Os números sorteados foram: {sorted(sorteio_lotofacil)}")

    def surpresinha(self): 
        for i in range (2):
            numeros_cartela_aleatoria = random.sample(range(1, 26), 18)
            self.numeros_cartela.append(sorted(numeros_cartela_aleatoria))
        print(f"Os números da sua cartela Surpresinha foram:\n {self.numeros_cartela}")    

    def resultado_surpresinha(self):
        print("\nRESULTADO SURPRESINHA")
        sorteio_surpresinha = random.sample(self.numeros_universo, 18)
        print(f"Os números sorteados foram: {sorted(sorteio_surpresinha)}")

def main():
    loteria = FormularioLoteria()

    while True:
        print("\n=$= Menu Principal =$=")
        print("1. LotoFacil Convencional")
        print("2. LotoFacil Surpresinha")

        formulario_opcao = input("\nEscolha uma opção: ")
        opcao = formulario_opcao.lower()
        
        if opcao == "1":
            loteria.quantidade_dezena()
            loteria.validar_cartela()
            loteria.resultado_loteria()
            break
        elif opcao == "2":
            loteria.surpresinha()
            loteria.resultado_surpresinha()
            break
        else:
            print("\nOpção inválida! Tente novamente.")
        
if __name__ == "__main__":

    main()