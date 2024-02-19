menu = """
************MENU***********

[0] Depósito
[1] Saque
[2] Extrato
[3] Sair

Selecione a opção desejada: """

saldo = 0
extrato = ""
LIMITE_SAQUES = 3
limite_dinheiro = 500
saque_atual = 0

while True:
    selecao = input(menu)
  
    if selecao == "0":
        print()
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito: .2f}\n"
            print("Depósito efetuado com sucesso!")
        else:
            print("Operação falhou! Valor digitado é inválido.")

    elif selecao == "1":
        print()
        saque = float(input("Digite o valor a ser sacado: "))

        if saque > limite_dinheiro:
            print("Valor de saque excede o limite.")

        elif saque > saldo:
            print("Valor excede saldo atual.")

        elif saque_atual >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saldo: .2f}\n"
            saque_atual += 1
            print("Saque efetuado com sucesso!")
        
        else:
            print("Operação falhou! Valor digitado é inválido.")

    elif selecao == "2":
        print()
        print("**********EXTRATO**********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        print("***************************")

    elif selecao == "3":
        break

    else:
        print("Opção inválida. Por favor digite um dos valores do menu.")

