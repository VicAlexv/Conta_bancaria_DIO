saldo = 0
limite = 500
LIMITE_SAQUES = 3


def Sacar(C):
    global saldo
    saldo -= C

def Depositar(C):
    global saldo
    saldo += C

def Extrato():
    global saldo
    print("saldo = R$ %.2f" % saldo)





def menu():
        print("--------------Olá, sejá bem vindo---------------")
        print("digite s para sacar dinheiro da conta")
        print("digite d para depositar dinheiro da conta")
        print("digite e para visualizar o extrato a conta")
        print("digite f para finalizar o programa")
        print("------------------------------------------------")
        
menu()

while True:

    op = str(input('Digite a operação desejada: '))

    if op=="s":
        if(LIMITE_SAQUES >0):
            C=float( input('Digite a quantia que deseja sacar: ') )
            if(C <= 500 and saldo >= C):
                Sacar(C)
            else:
                print("quantia acima do permitido ou do valor do saldo, portanto não foi possivel realizar a operação de saque")
            LIMITE_SAQUES-=1
        else:
            print("Você atingiu a quantia limite de saque, portanto não foi possível realizar a operação de saque")
    elif op=="d":
        C=float( input('Digite a quantia que deseja depositar: ') )
        if(C >= 0):
            Depositar(C)
        else:
            print("Não foi possivel realizar o depopsito")
    elif op=="e":
        Extrato()
    elif op == "f":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")