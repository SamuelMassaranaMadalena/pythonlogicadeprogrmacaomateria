n = 0
si = 0
sp = 0
while n < 1000:
    n = int(input("Digite um valor: "))
    if n > 1000:
        break
    if n % 2 == 0:
        sp = sp + n
    else:
        si = si + n
print(f"A soma dos números pares é {sp} e a soma dos números ímpares é {si}")