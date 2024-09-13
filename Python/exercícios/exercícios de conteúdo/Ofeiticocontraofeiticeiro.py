Qa = int(input("Qual a quantidade de quiloWatts/hora? "))
TP = str(input("Qual o tipo de instalação do lugar? "))
if TP == "R" and Qa <= 1000:
    if Qa <= 500:
        Qa * 0.40
    else:
        Qa * 0.65
elif TP == "C" and Qa <= 5000:
    if Qa <= 2500:
        Qa* 0.55
    else:
        Qa * 0.60
elif TP == "I" and Qa <= 15000:
    if Qa <= 10000:
        Qa * 0.55
    else:
        Qa * 0.60
else:
    print("Não é possível calcular")
print(Resultado)
