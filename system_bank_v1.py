menu = """
    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def sacar(valor: float):
    global numero_saques
    global saldo
    global extrato

    if numero_saques <= LIMITE_SAQUES:
        if saldo != 0 and saldo >= valor:
            saldo -= valor
            numero_saques += 1
            extrato = "{} Saque: {}\n".format(extrato, saldo)
        else:
            print("Seu saldo é insufiente!")
    else:
        print("Numero de saques excedido. Tente Novamente no dia seguinte.")


def depositar(valor: float):
    global extrato
    global saldo

    if valor > 0:
        saldo = valor
        extrato = "{} Deposito: {}\n".format(extrato, saldo)
    else:
        print('Nao e possivel adicionar um valor igual ou inferior a zero!')

def consultarExtrato():
    global extrato
    return '''
            Esse é seu extrado:

            Extrato: {}            
            '''.format(extrato)

while True:

    opcao = input(menu)

    if opcao == "s":
        print('Voce selecionou saque')
        sacar(float(input("Digite o valor a ser sacado: ")))

    elif opcao == "d":
        print('Voce selecionou depositar! \n')
        depositar(float(input("Digite o valor a ser depositado: ")))

    elif opcao == "e":
        print(consultarExtrato())
    elif opcao == "q":
        break
    else:
        print('Operacao invalida, por favor selecione uma operacao valida!')
    
        
