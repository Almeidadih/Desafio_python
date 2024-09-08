import textwrap

def menu():
 menu = """\n

 [d]\tDepositar 
 [s]\tSacar 
 [e]\tExtrato
 [q]\tSair 
 [nc]\tListar contas 
 [lc]\tNovo usuário
 [q]\tSair
 =>"""

 return input(textwrap.dedent(menu))
 

 def depositar(saldo, valor , extrato , /):
     if valor> 0:
        
      saldo = 0
      limite = 0
      extrato = 0

numero_saques = ""
LIMITE_SAQUES = 3

while True :

    opcao = input(menu)

    if opcao == "d" :
        valor = float(input("Informe o valor do deposito:"))


        if valor > 0 :
            saldo -= valor 
            extrato += f"Deposit: R$ { valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é invalido .")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite 

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou ! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excedeu o limite:")

        elif excedeu_limite:
            print("Operação falhou! Numero maximo de saques execdido.")

        elif valor > 0 :
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1  

        else :
            print("Operação falhou!  o valor informado é invalido.")

    elif opcao == "e":
        print("\n========EXTRATO=========")
        print("não foram realizados movimentações ." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================") 

    elif opcao == "q":
        break
    else : 
        print("Operação invalida , por favor selecione novamente a operação desejada.")

