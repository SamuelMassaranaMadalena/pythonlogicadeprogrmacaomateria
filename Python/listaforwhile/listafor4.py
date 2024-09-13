valor = int(input("Digite um valor: "))
for a in range(1, 100000000):
    if valor % a == 0:
        print (f"O número {a} é um divisor")
