# Obs.: Calcular e imprimir o nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias contratados.

print("=== Locadora de Veículos ===")

class FormularioClientes:
    def __init__(self):
        self.clientes = {}
        self.lista_clientes = []
        self.lista_km_contratados = []
        self.lista_mulheres_acima_sete_dias = []
                    # validacao
    def validar_sexo(self):
        while True:
            sexo = input("Digite o sexo do cliente (M/F): ").upper()
            if sexo in ['M', 'F']:
                return sexo
            print("Erro: Digite apenas 'M' para Masculino ou 'F' para Feminino.")

    def cadastrar_cliente(self):
        print("=== Cadastro de Cliente ===")

        nome = input("Digite o nome do cliente: ")
        sexo = self.validar_sexo()
        placa = input("Digite a placa do carro do cliente: ")
        km_contratados = float(input("Digite a quantidade de km contratados pelos clientes: "))
        dias_contratados = float(input("Digite quantos dias foram contratados pelo cliente: "))
        
        self.cliente = {
        'nome': nome, 
        'sexo': 'Masculino' if sexo == 'M' else 'Feminino', 
        'placa': placa,
        'kmcontratado': km_contratados, 
        'diascontrato': dias_contratados,
        'pagamentototal': (dias_contratados * 70) + (km_contratados * 0.10)
        }
                            # add itens listas
        self.lista_km_contratados.append(self.cliente['kmcontratado'])
        self.lista_clientes.append(self.cliente)
        if sexo == "F" and dias_contratados > 7:
            self.lista_mulheres_acima_sete_dias.append(self.cliente)

    def calcular_media_km(self):
        self.media_km = sum(self.lista_km_contratados) / len(self.lista_km_contratados)
        return self.media_km

    def imprimir_clientes(self):
        print("=== Lista de Cliente ===")

        if not self.lista_clientes:
            print("Nenhum cliente cadastrado.")
            return

        for i, cliente in enumerate(self.lista_clientes, 1):
            print(f"\nCliente {i}")
            print(f"Cliente: {cliente['nome']}")
            print(f"Placa: {cliente['placa']}")
            print(f"Total a pagar: {cliente['pagamentototal']}")

    def imprimir_media_km(self):
        print("\n ===Média de km contratados ===")

        media_km = self.calcular_media_km()
        print(f"A média de km contrados é {media_km:.1f}")

    def imprimir_mulheres_acima_sete_dias(self):
        print("\n ===Mulheres com contrato >7 dias ===")
   
        if not self.lista_mulheres_acima_sete_dias:
            print("Nenhuma cliente cadastrada com mais de sete dias de contrato.")
            return

        for i, cliente in enumerate(self.lista_mulheres_acima_sete_dias, 1):
            print(f"\nCliente {i}")
            print(f"Cliente: {cliente['nome']}")
            print(f"Placa: {cliente['placa']}")
            print(f"Total de dias: {cliente['diascontrato']}")

# interface
def main():
    formulario = FormularioClientes()

    while True:
        print("\n=== Menu Principal ===")
        print("1. Cadastrar novo cliente")
        print("2. Listar clientes")
        print("3. Listar clientes femininos que fecharam aluguéis acima de 7 dias")
        print("4. Ver média de km contratados")
        print("5. Sair")

        formulario_opcao = input("\nEscolha uma opção: ")
        opcao = formulario_opcao.lower()

        if opcao == "1":
            formulario.cadastrar_cliente()
        elif opcao == "2":
            formulario.imprimir_clientes()
        elif opcao == "3":
            formulario.imprimir_mulheres_acima_sete_dias()
        elif opcao == "4":
            formulario.imprimir_media_km()
        elif opcao == "5" or opcao == "sair": 
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()