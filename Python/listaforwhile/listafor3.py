a = int(input('Digite um valor para fatorar ele: '))
b = a - 1
for c in range(1, b):
    a = a * b
    b = b -1 
print(f'O resultado é {a}')