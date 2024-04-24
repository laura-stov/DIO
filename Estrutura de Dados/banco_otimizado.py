LIMITE = 500
LIMITE_SAQUES = 3

#por chave apenas (nome = "bla")
def saque(*, valor, saldo, extrato, numero_saques):

    if valor > saldo:
        print("A operação falhou! Você não tem saldo suficiente.")
    
    elif valor > LIMITE:
        print("A operação falhou! Limite insuficiente.")

    elif numero_saques >= LIMITE_SAQUES:
        print("A operação falhou! Você atingiu o limite de saques diários.")
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")

    else:
        print("A operação falhou! Digite um valor válido.")

    return saldo, extrato, numero_saques

#por posição apenas
def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("A operação falhou! Digite um valor válido.")
    
    return saldo, extrato

def extrato_final(saldo, /, *,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuario):
    cpf = input("Digite o seu CPF (somente números): ")
        
    if cpf in usuario:
        print("CPF já cadastrado!")
    else:
        nome = input("Digite seu nome completo: ")
        data = input("Digite sua data de nascimento no formato (dd/mm/aaaa): ")
        endereco = input("Digite o seu endereco no formato (logradouro, nro - bairro, cidade/sigla estado): ")
        usuario.extend([cpf, nome, data, endereco])

    return usuario

def criar_conta(usuario, num_conta, conta_total):
    agencia = "0001"

    cpf = input("Digite o número do seu CPF: ")
    if cpf not in usuario:
        print("Usuário não encontrado!")
    else:
        num_conta += 1
        conta = [agencia, num_conta, usuario]
        conta_total.append(conta)
        
    return conta_total, num_conta

def capital(num_conta, numero_saques, extrato, saldo, dados_total):
    dados = {"Conta": num_conta, "Saldo": saldo, "Número de saques feitos": numero_saques, "Extrato": extrato}
    dados_total.append(dados)
    
    return dados_total

menu1 = """
    [1] Acessar conta
    [2] Criar usuário
    [3] Criar conta
    [0] Sair
  
=> """

menu2 = """
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair

=> """

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuario = []
    num_conta = 0
    conta_total = []
    dados_total = []

    while True:
        opcao = int(input(menu1))

        if opcao == 1:
            cpf = input("Digite seu CPF: ")

            if cpf not in usuario:
                print("Usuário não encontrado.")
            
            else:
                print("Você possui as seguintes contas: ")
                
                numero = []
                for conta in conta_total:
                    aux = conta[1]
                    numero.append(aux)
                    print(aux, end=" ")

                selecao = int(input("\nDigite a conta a ser acessada: "))

                if selecao not in numero:
                    print("Digite uma opção válida.")

                else:   
                    indice = selecao - numero[0]

                    saldo = dados_total[indice].get("Saldo")
                    extrato = dados_total[indice].get("Extrato")
                    numero_saques = dados_total[indice].get("Número de saques feitos")

                    while True:
                        dados_total[indice].update({"Saldo": saldo})
                        dados_total[indice].update({"Número de saques feitos": numero_saques})
                        dados_total[indice].update({"Extrato": extrato})
                        
                        opcao = int(input(menu2))

                        if opcao == 1:
                            valor = float(input("Digite o valor a ser sacado: "))
                            print()
                            saldo, extrato, numero_saques = saque(valor = valor, saldo = saldo, extrato = extrato, numero_saques = numero_saques)

                        elif opcao == 2:
                            valor = float(input("Digite o valor a ser depositado: "))
                            print()
                            saldo, extrato = deposito(valor, saldo, extrato)

                        elif opcao == 3:
                            extrato_final(saldo, extrato = extrato)
                            print()

                        elif opcao == 0:
                            break

                        else:
                            print("Digite uma opção válida!")
                            print()

        elif opcao == 2:
            usuario = criar_usuario(usuario)
            print("Usuário criado com sucesso!")

        elif opcao == 3:
            conta_total, num_conta = criar_conta(usuario, num_conta, conta_total)
            dados_total = capital(num_conta, 0, "", 0, dados_total)

            print("Conta criada com sucesso!")

        elif opcao == 0:
            break

        else:
            print("Digite uma opção válida!")
   
main()
