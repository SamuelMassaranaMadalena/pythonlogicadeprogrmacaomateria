'''
def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x):
        return "Par"
    else:
        return "Impar"

print(epar(2), par_ou_impar(2))
print(epar(3), par_ou_impar(3))
print(epar(10), par_ou_impar(10))

def soma(a, b):
    return a + b 

print(soma(1, 3))
'''

a = 5 #variável global
def  muda_e_imprime():
    global a #variável global
    a = 7
    print(f"a dentro da funcção {a}")

print(f"a antes de mudar: {a}")
muda_e_imprime()
print(f"a depois de mudar: {a}")
