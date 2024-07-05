saldo = 0
limite = 500
limite_saques = 3
lista_usuarios = []
lista_contas = []
extrato = ""
numero_conta = 1
agencia = "0001"


def Sacar(*,valor,extrato):
    global saldo
    saldo -= valor
    extrato = f"foi sacado R${valor:.2f} de sua conta"
    print(extrato)

def Depositar(C, extrato, /):
    global saldo
    saldo += C
    extrato = f"foi depositado R${C:.2f} em sua conta"
    print(extrato)

def Extrato(saldo,/,*,extrato):
    extrato = f"saldo = R${saldo:.2f}"
    print(extrato)

def CriarConta(C,agencia, np, usuarios,contas):
    global numero_conta
    cpf_existente = False
    for indice, usuario in enumerate(usuarios):
        if usuario["cpf"] == C:
            cpf_existente = True
            numero_usuario = indice                 
    if cpf_existente:
        contas.append({"agencia": agencia,"numero_conta": np,"numero_usuario": numero_usuario})
        np +=1
        numero_conta = np
        print(contas)
        print("conta cadastrado com sucesso")
        

def CriarUsuario(C,N,D,E, usuarios):
    usuarios.append({"cpf": C,"nome": N,"data": D,"endereco": E})
    print(usuarios)
    print("usuario cadastrado com sucesso")



def menu():
        print("--------------Olá, sejá bem vindo---------------")
        print("digite u para cadastrar um novo usuário")
        print("digite c para criar uma nova conta")
        print("digite s para sacar dinheiro da conta")
        print("digite d para depositar dinheiro da conta")
        print("digite e para visualizar o extrato a conta")
        print("digite f para finalizar o programa")
        print("------------------------------------------------")
        
menu()

while True:

    op = str(input('Digite a operação desejada: '))

    if op=="s":
        if(limite_saques >0):
            C=float( input('Digite a quantia que deseja sacar: ') )
            if(C <= 500 and saldo >= C):
                Sacar(valor = C, extrato = extrato)
            else:
                print("quantia acima do permitido ou do valor do saldo, portanto não foi possivel realizar a operação de saque")
            limite_saques-=1
        else:
            print("Você atingiu a quantia limite de saque, portanto não foi possível realizar a operação de saque")
    
    elif op=="d":
        C=float( input('Digite a quantia que deseja depositar: ') )
        if(C >= 0):
            Depositar(C, extrato)
        else:
            print("Não foi possivel realizar o depopsito")
    
    elif op=="e":
        Extrato(saldo, extrato = extrato)
    
    elif op == "f":
        break
    
    elif op=="u":
        tamanho = 0
        C=str( input('Digite seu CPF: ') )
        if not lista_usuarios:
            N=str( input('Digite seu nome: ') )
            D=str( input('Digite a data de seu nascimeto: ') )
            E=str( input('Digite seu endereço: ') )
            CriarUsuario(C,N,D,E, lista_usuarios)
        else:
            cpf_existente = False
            for usuario in lista_usuarios:
                if usuario["cpf"] == C:
                    cpf_existente = True
                    
            if cpf_existente:
                print("Usuario já cadastrado")
            else:
                N=str( input('Digite seu nome: ') )
                D=str( input('Digite a data de seu nascimeto: ') )
                E=str( input('Digite seu endereço: ') )
                CriarUsuario(C,N,D,E, lista_usuarios)
    
    elif op=="c":
        nc = numero_conta
        C=str( input('Digite seu CPF: ') )
        CriarConta(C,agencia,nc,lista_usuarios,lista_contas)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")