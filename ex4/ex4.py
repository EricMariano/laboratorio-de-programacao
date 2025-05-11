# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.

# a) O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e 
# passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá
# este valor ao programa que a chamou.
# 
# b) O programa deverá então exibir o valor a ser pago na tela.

# c) Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até 
# que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e
# o valor total de prestações pagas no dia.
# 
# d) O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação;
# quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

from dataclasses import dataclass

@dataclass
class ProcessarPagamento:
    quantidade_prestacoes: int = 0
    valor_total_pago: float = 0

    def valorPagamento(self, valor_prestacao: float, dias_atraso: int) -> float:
        if dias_atraso <= 0:
            return valor_prestacao
        else:
            multa = valor_prestacao * 0.03
            juros = valor_prestacao * (0.001 * dias_atraso)
            return valor_prestacao + multa + juros
    
    def registrar_pagamento(self, valor: float):
        self.quantidade_prestacoes += 1
        self.valor_total_pago += valor
    
    def gerar_relatorio(self):
        return f"\nRELATÓRIO DO DIA\n" \
               f"Quantidade de prestações pagas: {self.quantidade_prestacoes}\n" \
               f"Valor total pago: R$ {self.valor_total_pago:.2f}"

def main():
    processador = ProcessarPagamento()
    
    while True:
        try:
            valor_prestacao = float(input("\nInforme o valor da prestação (0 para sair): R$ "))
            
            if valor_prestacao == 0:
                print(processador.gerar_relatorio())
                break
            
            dias_atraso = int(input("Informe o número de dias em atraso: "))
            
            valor_pago = processador.valorPagamento(valor_prestacao, dias_atraso)
            
            print(f"Valor a ser pago: R$ {valor_pago:.2f}")
            
            processador.registrar_pagamento(valor_pago)
            
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
