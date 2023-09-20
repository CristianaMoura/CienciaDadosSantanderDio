menu = """
    [1] Depositar,
    [2] Sacar,
    [3] Extrato,
    [0] Sair,
    """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUE = 3

while True :
    
    opcao = input(menu)
    if opcao == "1" :
        deposito = float(input("Digite o valor de depósito: "))
        if deposito < 0:
         print("Valor inválido") 
        else:          
            saldo += deposito
        extrato +=f"Depósito: R$ {deposito:.2f}\n"
        print(f"Seu saldo atual é R$ {saldo:.2f}")
                 
          
    elif opcao == "2" :
             
            if numero_saques >= LIMITES_SAQUE :
                print("Excedeu quantidade permitida de saque diária, volte amanhã!")  
            else :
                            
                valor_saque = float(input("Digite o valor do Saque: \n"))
                if valor_saque <= limite:
                                
                  saldo -= valor_saque
                  numero_saques +=1
                else:
                  print("Excedeu seu limite de valor de saque diário, volte amanhã")
                  
            extrato +=f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Seu saldo atual é R$ {saldo:.2f}")  


    elif opcao == "3" :
            
            print("--------------EXTRATO-------------------\n")
            print(extrato)
            print("-----------------------------------------")
    
    elif opcao == "0" :
            print("Obrigada por escolher nossos serviços!")
            break

    else:
           print("Operação inválida, por favor selecione novamente a opção desejada.")        
        

            
