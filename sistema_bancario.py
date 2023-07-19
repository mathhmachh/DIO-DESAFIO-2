import textwrap

def menu():
    menu = """

    [1]\tDEPOSITAR
    [2]\tSACAR
    [3]\tEXTRATO
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("Falha na operação! Informe um valor válido.")
        
        return(saldo, extrato)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
             print("Não há saldo suficiente para essa operação.")

        elif excedeu_limite:
            print("Limite por operacao ultrapassado.")

        elif excedeu_saques:
            print("Você exceudeu seu número de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("Operação falhou! O valor informado é invalido.")

        return saldo, extrato

def extrato(saldo, /, *, extrato):
        
        print ("\n==============EXTRATO==============") 
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")        

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n Já existe um usuário com esse CPF!")
         return
    
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informear o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
         print("\n=== Conta criada com sucesso! ===")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário nao encontrado, fluxo de criacao de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
         linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
         print("=" * 100)
         print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
