Qa = int(input("Qual a quantidade de quiloWatts/hora? "))
TP = str(input("Qual o tipo de instalação do lugar? "))
Resultado = int()
if TP == "R" or TP == "Residencial" or TP == "r" or TP == "residencial" and Qa <= 1000:
    if Qa <= 500:
        Resultado = Qa * 0.40
    else:
        Resultado = Qa * 0.65
elif TP == "C" or TP == "Comercial" or TP == "c" or TP == "comercial" and Qa <= 5000:
    if Qa <= 2500:
        Resultado = Qa* 0.55
    else:
        Resultado = Qa * 0.60
else:
    if TP == "I" or TP == "Industrial" or TP == "i" or TP == "industrial" and Qa <= 15000:
        if Qa <= 10000:
            Resultado = Qa * 0.55
        else:
            Resultado = Qa * 0.60
    else:
        print("Não é possível calcular")
if Resultado> 0:
    print(Resultado)
