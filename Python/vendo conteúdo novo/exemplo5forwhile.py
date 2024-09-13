n = int(0)
s = str()
for s in range(10):
    s = str(input("Digite o seu sexo/genêro: "))
    if s == "M" or s == "m":
        n = n + 1
    elif s == "Masculino" or s =="masculino":
        n = n +1
print(f"{n} pessoas são do sexo masculino")
