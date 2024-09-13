def eh_positivo(a):
    if a >= 0:
        return True
    else:
        return False
valor = int(input("Digite um valor"))
print(eh_positivo(valor))