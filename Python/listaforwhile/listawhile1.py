media = 0
b = 0
a = int(0)
while a >= 0:
    a = int(input("Digite um valor: "))
    if a < 0:
        break
    media = media + a
    b = b + 1
print(f"A média dos valores é {media/b} e a soma deles é {media} ")