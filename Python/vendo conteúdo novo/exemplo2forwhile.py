'''
a = int()
n = int(0)
while a >= 0:
    a = int(input("Digite um número"))
    if a < 0:
        break
    n = n + 1
print(f"Você digitou {n} números")
'''
n = int()
for a in range(1000):
    a = int(input("Digite um número: "))
    if a < 0:
        break
    n = n + 1
print(f"Você digitou {n} números")