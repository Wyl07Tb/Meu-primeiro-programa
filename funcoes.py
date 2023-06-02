def apresentacao_f():
    print("Olá, bem vindo! Sou o Caixinha! Seu assistente de caixa virtual.")
    print()
    print("Para iniciar, informe o número da opção desejada!")

def compra_f(tot):
    print()
    vezes = int(input("Agora digite quantas vezes essa função foi usada: "))
    print(vezes, "vezes, Ok!")
    print()
    atual = 0
    total = tot
    for compras in range(vezes):
        compra = float(input("Incira o valor da compra e confirme: "))   
        atual += compra
        total += compra
    print()
    print("O montante atual é de: R$",atual)
    print("O montante total é de: R$",total)
    return vezes, atual

def dinheiro():
    print("(Dinheiro), Ok!")
    print()
    print("Agora digite, qual a espécie desejada!")
    especie = int(input("1.(Notas), 2.(Moedas): "))
    return especie

def valor_em_notas(tot):
    print("Valor em (Notas), Ok!")
    print()
    print("Qual o valor da nota?")
    valor = int(input("2Reais, 5Reais, 10Reais, 20Reais, 50Reais, 100Reais ou 200Reais: "))
    if (valor == 2) or (valor == 5) or (valor == 10) or (valor == 20) or (valor == 50) or(valor == 100) or(valor == 200):
        print(valor, "reais, Ok!")
        print()
        quant = 0
        sub_total = tot
        quant = int(input(f"Quantas notas de {valor} reais você tem?: "))
        valor = valor * quant
        print(f"Você tem o valor de: (R${valor:.2f}) em notas atualmente!")
        total = valor + sub_total
        print(f"E o valor total de: (R${total:.2f}) em notas!")
    else:
        print("Ops... Valor inesistente! Por favor, digite apenas o númeoro sem (CARACTERES ou LETRAS!)")
    return total, quant
    
def valor_em_moedas(tot):
    print("Valor em (Moedas), Ok!")
    print()
    print("Qual o valor da moeda?")
    valor = int(input("5Centavos, 10Centavos, 25Centavos, 50Centavos ou 1Real: "))
    if (valor == 5) or (valor == 10) or (valor == 25) or (valor == 50):
        valor = valor / 100
        print(f"{valor:.2f}centavos, Ok!")
        print()
        quant = 0
        sub_total = tot
        quant = int(input(f"Quantas moedas de {valor} centavos você tem?: "))
        valor = valor * quant
        print(f"Você tem o total de: (R${valor:.2f}) em moedas!")
    elif valor == 1:
        print(valor, "real, Ok!")
        quant = int(input(f"Quantas moedas de {valor} real você tem?: "))
        valor = valor * quant
        print(f"Você tem o valor de: (R${valor:.2f}) em moedas atualmente!")
        total = valor + sub_total
        print(f"E o valor total de: (R${total:.2f}) em moedas!")
    else:
        print("Ops... Valor inesistente! Por favor, digite apenas o númeor sem (CARACTERS ou LETRAS!)")
    return total, quant