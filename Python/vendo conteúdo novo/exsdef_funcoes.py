def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x):
        return "Par"
    else:
        return "Impar"
print(par_ou_impar(4))
print(par_ou_impar(5))


a = 5 #variável global
def muda_e_imprime():
    global a #variável global
    a = 7
    print(f"a dentro da função: {a}")

print(f"a antes de mudar: {a}")
muda_e_imprime()
print(f"a depois de mudar: {a}")