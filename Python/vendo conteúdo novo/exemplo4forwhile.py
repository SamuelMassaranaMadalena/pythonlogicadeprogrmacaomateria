n = int(0)
print("*O número 0 encerra esta parte do programa* \n")
for a in range(1000):
    a = int(input("Digite um número: "))
    if a >= 100 and a <= 200:
        n = n + 1
    if a == 0:
        break
print(f'{n} números entre 100 e 200 foram digitados')