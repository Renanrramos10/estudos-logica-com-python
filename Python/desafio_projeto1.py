menu = '''

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

'''
saldo = 1500
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")

    elif opcao == "2":
        print("Saque")
        valor =input("Quanto deseja sacar?")
        valor = "R${valor}" 
        if limite >= valor:
            print("Você realizou seu saque de:{valor}")

    elif opcao == "3":  
        print()
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


