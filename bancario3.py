from datetime import date

class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = 3

    def sacar(self, valor):
        if self.limite_saques > 0 and (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            self.limite_saques -= 1
            return True
        return False

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        print(f"Depositado R${self.valor:.2f} na conta {conta.numero}")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        print(f"Sacado R${self.valor:.2f} da conta {conta.numero}")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

def cadastrar_usuario(usuarios):
    cpf = input('Digite seu CPF: ')
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Usuário já cadastrado.")
            return usuario
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite a data de seu nascimento: ')
    endereco = input('Digite seu endereço: ')
    novo_usuario = Cliente(cpf, nome, data_nascimento, endereco)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")
    return novo_usuario

def criar_conta(clientes, agencia, numero_conta):
    cpf = input('Digite seu CPF: ')
    for cliente in clientes:
        if cliente.cpf == cpf:
            limite = float(input('Digite o limite da conta corrente: '))
            conta = ContaCorrente(numero_conta, agencia, cliente, limite)
            cliente.adicionar_conta(conta)
            print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
            return conta
    print("Cliente não encontrado.")
    return None

def sacar(conta):
    valor = float(input('Digite o valor que deseja sacar: '))
    if conta.sacar(valor):
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Não foi possível realizar o saque.")

def depositar(conta):
    valor = float(input('Digite o valor que deseja depositar: '))
    if conta.depositar(valor):
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Não foi possível realizar o depósito.")

def extrato(conta):
    print(f"Saldo atual da conta {conta.numero}: R${conta.saldo:.2f}")

def menu():
    print("--------------Bem-vindo ao sistema bancário---------------")
    print("Digite u para cadastrar um novo usuário")
    print("Digite c para criar uma nova conta")
    print("Digite s para sacar dinheiro da conta")
    print("Digite d para depositar dinheiro na conta")
    print("Digite e para visualizar o extrato da conta")
    print("Digite f para finalizar o programa")
    print("-----------------------------------------------------------")

clientes = []
numero_conta = 1
agencia = "0001"

while True:
    menu()
    op = input('Digite a operação desejada: ').lower()

    if op == "s":
        cpf = input('Digite seu CPF: ')
        for cliente in clientes:
            if cliente.cpf == cpf:
                conta_encontrada = None
                for conta in cliente.contas:
                    if isinstance(conta, ContaCorrente):
                        conta_encontrada = conta
                        break
                if conta_encontrada:
                    sacar(conta_encontrada)
                else:
                    print("Você não possui uma conta corrente para saque.")
                break
        else:
            print("Cliente não encontrado.")

    elif op == "d":
        cpf = input('Digite seu CPF: ')
        for cliente in clientes:
            if cliente.cpf == cpf:
                conta_encontrada = None
                for conta in cliente.contas:
                    if isinstance(conta, ContaCorrente):
                        conta_encontrada = conta
                        break 
                if conta_encontrada:
                    depositar(conta_encontrada)
                else:
                    print("Você não possui uma conta corrente para depósito.")
                break  
        else:
            print("Cliente não encontrado.")

    elif op == "e":
        cpf = input('Digite seu CPF: ')
        for cliente in clientes:
            if cliente.cpf == cpf:
                conta_encontrada = None
                for conta in cliente.contas:
                    if isinstance(conta, ContaCorrente):
                        conta_encontrada = conta
                        break 
                if conta_encontrada:
                    extrato(conta_encontrada)
                else:
                    print("Você não possui uma conta corrente para extrato.")
                break  
        else:
            print("Cliente não encontrado.")

    elif op == "f":
        print("Programa finalizado.")
        break

    elif op == "u":
        cadastrar_usuario(clientes)

    elif op == "c":
        criar_conta(clientes, agencia, numero_conta)
        numero_conta += 1

    else:
        print("Operação inválida. Por favor, selecione uma operação válida.")
