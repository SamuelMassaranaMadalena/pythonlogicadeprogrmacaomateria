menor = 1000000000000000000000000000000000000
maior = 0
a = 0
print("Valores negativos encerram o programa")
while a >= 0:
    a = int(input("Digite um valor: "))
    if a < 0:
        break
    if a > maior:
        maior = a
    if a < menor:
        menor = a
if menor == maior:
    print(f'O menor e o maior valor foram {menor}')
else: 
    print(f"O menor valor é {menor} e o maior é {maior}")