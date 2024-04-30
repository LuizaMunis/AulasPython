class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}, \nCPF: {self.cpf}"


class Historico:
    def __init__(self, data_abertura):
        self.data_abertura = data_abertura
        self.transacoes = []

    def imprime(self):
        return f"{self.transacoes}"


class ContaBancaria:
    contas = []

    def __init__(self, Cliente, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico("24/04/2024")
        self.cliente= Cliente
        ContaBancaria.contas.append(self)

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        self.saldo -= valor
        self.historico.transacoes.append(f"Saque:-{valor}")
        return self.saldo

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Deposito:{valor}")
        return self.saldo

    def obter_extrato(self):
        return self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.cliente.nome = novo_titular

    def transfere_para(self, destino, valor):
        for conta in ContaBancaria.contas:
            if conta.cliente.nome == destino:
                if self.saldo >= valor:
                    self.saldo -= valor
                    conta.saldo += valor
                    print("Transferência realizada com sucesso!")
                    return
                else:
                    print("Saldo insuficiente para realizar a transferência.")
                    return
        print("Conta de destino não encontrada.")

    def fechar_conta(self, nome_conta_cancelar):
        nome_conta_cancelar = input("Digite o nome da conta que deseja cancelar")
        if self.cliente.nome == nome_conta_cancelar:
            ContaBancaria.contas.remove(self)
            print("Conta cancelada com sucesso.")


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self, saldo):
        taxa_anual = 0.5 / 365
        juros_diario = saldo * taxa_anual
        self.historico.transacoes.append(f"juros:+{juros_diario}")
        return juros_diario


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial


def menu():
    print("Menu:")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Obter extrato")
    print("5. Transferir para outra conta")
    print("6. Fechar conta")
    print("0. Sair")
opcao=None

cliente1 = Cliente("Pebinha", "Silva", "123.456.789-00")
conta = ContaBancaria(cliente1, numero_agencia="896523", tipo_conta="Corrente", saldo=2000, limite=1000)

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Saldo atual:", conta.consultar_saldo())
        
    elif opcao == 2:
        valor = float(input("Digite o valor a sacar: "))
        print("Novo saldo:", conta.saca(valor))
        
    elif opcao == 3:
        valor = float(input("Digite o valor a depositar: "))
        print("Novo saldo:", conta.deposita(valor))
        
    elif opcao == 4:
        print("Extrato:", conta.obter_extrato())
        
    elif opcao == 5:
        destino = input("Digite o nome do destinatário: ")
        valor = float(input("Digite o valor a transferir: "))
        conta.transfere_para(destino, valor)
        
    elif opcao == 6:
        conta.fechar_conta()
        
    elif opcao == 0:
        print("Saindo...")
        
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")