from funcoes import *
apresentacao_f()
#Bloco para coleta das quantidades referente a cada valor.
vezes_no_cred = 0
total_cred = 0
vezes_no_deb = 0
total_deb = 0
while True:
    print()
    funcao = int(input("1.(Crédito), 2.(Débito), 3.(Dinheiro) 4.(Balanso diário), 5.(Finalizar o programa): "))

#Início do bloco de coleta de dados referente a função (Crédito).
    if funcao == 1:
        print("(Crédito), Ok!")
        mais_vezes, mais_atual = compra_f(total_cred)
        vezes_no_cred += mais_vezes
        total_cred += mais_atual

#Início do bloco de coleta de dados referente a função (Débito).
    elif funcao == 2:
        print("(Débito), Ok!")
        mais_vezes, mais_atual = compra_f(total_deb)
        vezes_no_deb += mais_vezes
        total_deb += mais_atual

#Início do bloco de coleta de dados referente a função (Dinheiro).
    elif funcao == 3:
        print("(Dinheiro), Ok!")
        print()
        print("Agora digite, qual a espécie desejada!")
        especie = int(input("1.(Notas), 2.(Moedas): "))
        #Início do bloco de coleta de dados referente a função (Notas).
        if especie == 1:
            print("Valor em (Notas), Ok!")
            print()
            print("Qual o valor da nota?")
            valor = int(input("2Reais, 5Reais, 10Reais, 20Reais, 50Reais, 100Reais ou 200Reais: "))
            print(valor, "reais, Ok!")
        #Início do bloco de coleta de dados referente a função (Moedas).
        elif especie == 2:
            print("Valor em (Moedas), Ok!")
            print()
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
        print()
        print("Opção: Crédito")
        print("A função crédito foi utilizada (",vezes_no_cred,") vezes hoje. Resultando no montante total de:(R$",total_cred,")")
        print()
        print("Opção: Débito")
        print("A função (DÉBITO) foi utilizada (",vezes_no_deb,") vezes hoje. Resultando no montante total de:(R$",total_deb,")")
    elif funcao == 5:
        print("Até a próxima... Tchal!")
        break
    else:
        print("Ops... Por favor; Digite apenas o número referente a uma das opções!")

#Criado por Wyllon Alencar! Contato: (48) 98845-1165.