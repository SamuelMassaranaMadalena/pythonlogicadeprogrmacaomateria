"""vendo conteúdo novo\
a = int(input("digite um número"))
while a != 999:
    a = a * 3
    print(a)
    a = int(input("Digite um valor e o triplo dele aparecerá, digite 999 para encerrar o programa"))
"""
for a in range(1000):
    a = int(input("digite um valor para mostrar seu triplo, o número 999 faz com que o programa se encerre"))
    b = a
    a = b
    a = a * 3
    print(a)
    