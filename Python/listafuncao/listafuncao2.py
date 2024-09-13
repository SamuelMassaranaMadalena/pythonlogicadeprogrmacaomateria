def eh_nulo(a):
    if a == "":
        return True
    else:
        return False
valor = input("Digite (ou não digite) algo")
print(eh_nulo(valor))