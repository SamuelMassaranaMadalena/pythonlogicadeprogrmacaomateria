idade = 0
m21 = 0
M50 = 0
while idade != -99:
    idade = int(input("Quantos anos você tem? "))
    if idade == -99:
        break
    if idade < 21:
        m21 = m21 + 1
    elif idade > 50:
        M50 = M50 + 1

print(f"{m21} pessoas tem menos de 21 anos e {M50} pessoas tem mais de 50 anos")