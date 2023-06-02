from funcoes import *   
apresentacao_f()
#Bloco para coleta das quantidades referente a cada valor.
vezes_no_cred = 0
total_cred = 0
vezes_no_deb = 0
total_deb = 0
quant_notas = 0
total_din_notas = 0
quant_moedas = 0
total_din_moedas = 0
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
        especie = dinheiro()
        #Início do bloco de coleta de dados referente a função (Notas).
        if especie == 1:
            valor_atual, quant = valor_em_notas(total_din_notas)
            quant_notas += quant
            total_din_notas += valor_atual
        #Início do bloco de coleta de dados referente a função (Moedas).
        elif especie == 2:
            valor_atual, quant = valor_em_moedas(total_din_moedas)
            quant_moedas += quant
            total_din_moedas += valor_atual
        else:
            print("Ops... Por favor; Digite apenas o número referente a uma das opções!")
    elif funcao == 4:
        print()
        print("Crédito")
        print("A função crédito foi utilizada (",vezes_no_cred,") vezes hoje. Resultando no montante total de:(R$",total_cred,")")
        print()
        print("Débito")
        print("A função (DÉBITO) foi utilizada (",vezes_no_deb,") vezes hoje. Resultando no montante total de:(R$",total_deb,")")
        print()
        print("Dinheiro")
        print("Você tem o total de: (R$",total_din_notas," em notas e (R$",total_din_moedas,") em moedas")
        
    elif funcao == 5:
        print("Até a próxima... Tchal!")
        break
    else:
        print("Ops... Por favor; Digite apenas o número referente a uma das opções!")

#Criado por Wyllon Alencar! Contato: (48) 98845-1165.