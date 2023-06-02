#Bloco para coleta das quantidades referente a cada valor.
print("Olá, bem vindo!")
print("Para iniciar, celecione o tipo desejado.")
total_credito = 0
quantidade_credito = 0
total_debito = 0
quantidade_debito = 0
while True:
    funcao = int(input("1.(Crédito), 2.(Débito), 3.(Dinheiro) 4.(Balanso diário), 5.(Finalizar o programa): "))
#Início do bloco de coleta de dados referente a função (Crédito).
    if funcao == 1:
        print("(Crédito), Ok!")
        vezes01 = int(input("Agora digite quantas vezes essa função foi usada: "))
        print(vezes01, "vezes, Ok!")
        credito_atual = 0
        quantidade_credito += vezes01
        for credito in range(vezes01):
            compras = float(input("Incira o valor da compra e confirme: "))
            total_credito += compras
            credito_atual += compras
        print(credito_atual)
        print(total_credito)
#Início do bloco de coleta de dados referente a função (Débito).
    elif funcao == 2:
        print("(Débito), Ok!")
        vezes02 = int(input("Agora digite quantas vezes essa função foi usada: "))
        print(vezes02, "vezes, Ok!")
        debito_atual = 0
        quantidade_debito += vezes02
        for debito in range(vezes02):
            compras = float(input("Incira o valor da compra e confirme: "))
            total_debito += compras
            debito_atual += compras
        print(debito_atual)
        print(total_debito)
#Início do bloco de coleta de dados referente a função (Dinheiro).
    elif funcao == 3:
        print("(Dinheiro), Ok!")
        print("Agora digite, qual a espécie desejada!")
        especie = int(input("1.(Notas), 2.(Moedas): "))
        #Início do bloco de coleta de dados referente a função (Notas).
        if especie == 1:
            print("Valor em (Notas), Ok!")
            print("Qual o valor da nota?")
            valor = int(input("2Reais, 5Reais, 10Reais, 20Reais, 50Reais, 100Reais ou 200Reais: "))
            print(valor, "reais, Ok!")
        #Início do bloco de coleta de dados referente a função (Moedas).
        elif especie == 2:
            print("Valor em (Moedas), Ok!")
            print("Qual o valor da moeda?")
            valor = int(input("5Centavos, 10Centavos, 25Centavos, 50Centavos ou 1Real: "))
            if (valor == 5) or (valor == 10) or (valor == 25) or (valor == 50):
                print(valor, "centavos, Ok!")
                int(input(f"Quantas moedas de {valor} centavos você tem?: "))
            elif valor == 1:
                print(valor, "real, Ok!")
                int(input(f"Quantas moedas de {valor} real você tem?: "))
            else:
                print("Ops... Valor inesistente! Por favor, digite apenas o númeor sem ( , ou . )")
        else:
            print("Ops... Por favor; Digite apenas o número referente a uma das opções!")
    elif funcao == 4:
        print("Crédito")
        print("A função CRÉDITO foi utilizada:", quantidade_credito, "vezes hoje. Com um montante total de: R$",total_credito)
        print("Débito")
        print("A função DÉBITO foi utilizada:", quantidade_debito, "vezes hoje. Com um montante total de: R$",total_debito)    
    elif funcao == 5:
        print("Até a próxima... Tchal!")
        break
    else:
        print("Ops... Por favor; Digite apenas o número referente a uma das opções!")
        
#Criado por Wyllon Alencar! Contato: (48) 98845-1165.