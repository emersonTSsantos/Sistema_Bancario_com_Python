menu = """

    ********* Escolha uma das opções *********

        (1) Depositar
        (2) Sacar (ATENÇÃO: Limite saque diário de até 3 vezes,Limite valor R$ 500.00.
        (3) Extrato
        (0) Sair

""" 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

valor_saque = 0
deposito = 0
saque = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito < 0:
            deposito -= deposito
            print("Operação falhou, valor informado inválido")

        

        if deposito != saldo or deposito > saldo:
            saldo += deposito
            extrato += f"depósito R$ +{deposito:.2f}\n"

            opcao = (input(f"""
                            Depósio executado com sucesso
                            saldo final: {saldo:.2f}

                            (5) Imprimir comprovante
                            (0) Encerrar sessão
                    """))
        
        if opcao == "5":
            print(f"""
                **************  COMPROVANTE **************
                
                    Depósitos de +R$ {deposito:.2f}.

                    Saldo total: R$ {saldo:.2f}

                ******************************************
                    """)

            
    elif opcao == "2":

        while numero_saques < LIMITE_SAQUES:

            numero_saques += 1

            valor_saque = float(input("Informe o valor de saque: "))


            if valor_saque > limite:
                    numero_saques -= 1
                    print(f"""
            
                        ATENÇAO: Você ultapassou limite de saque de R$ 500 reais.
                        Fique tranquilo !!
                        Suas chances de saques não foram descontadas, tente novamente.
                        """)
                    break
            
            if valor_saque > saldo:
                numero_saques -= 1
                print(f"""
            
                        ATENÇAO: Seu saldo é insuficiente.
                        Fique tranquilo !!
                        Suas chances de saques não foram descontadas, tente novamente.
                        """)
                break
                
            if numero_saques == LIMITE_SAQUES:
                print("Você ultrapassou limite de saque diário, tente novamente amanhã")
                

            if valor_saque < 0:
                valor_saque -= valor_saque

                print(f"""
            
                        Operação falhou, valor informado inválido
                        Fique tranquilo !!
                        Suas chances de saques não foram descontadas, tente novamente.
                        """)
                break
            
            if valor_saque <= limite:
                saldo -= valor_saque
                saque += valor_saque
                extrato += f"saque: R$: -{valor_saque:.2f}\n"

                print(f'Valor de saldo atual: R$ {saldo:.2f}')
                opcao = input((f"""
                                (1) Encerrar sessão
                                (2) Fazer outro saque

                                ATENÇÃO !! Você já usou {numero_saques} de saques hoje
                                Seu limite é de 3 diários.
                            """))
                if opcao == "1":
                    break
    elif opcao == "3":
        print("\n****************** EXTRATOS ******************")
        print("Nenhuma operação realizada" if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("***********************************************")
    elif opcao == "0":
        print("Sair")
        break
    else:
        print("Opcão não encontrada, tente Novamente")