n = int(0)
media = float(0)
for a in range(1000):
    a = int(input("O número 9999999 é que termina esta parte do programa \nDigite um número: "))
    if a == 9999999:
        break
    if a < 0:
        while a < 0:
            print("\nneste programa não estámos possibilitando a entrada de números negativos. \nPor favor digite um número positivo")
            a = int(input("O número 9999999 é o número que encerra esta parte do programa \ndigite um número: "))
    n = n + 1
    media = (a + media)
print(f"a média dos números digitados é {media/n:.2f}")