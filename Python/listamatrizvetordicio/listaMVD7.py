def par(a): #função para determinar se um valor é par ou não
    if (a % 2 == 0):
        return True
    else:
        return False
V = [9, 8, 7, 12, 0, 13, 21]
x = 0
p = []
i = []
x1 = 0
x2 = 0
while x < 7:
    if (par(V[x])) == True: #se a função retornar True ele copia esse elemento para o vetor de pares, senão ela copia para a matriz dos impares
        p.append(V[x])
        x1 += 1
    else:
        i.append(V[x])
        x2 += 1
    x += 1
print(f"I {i}") 
print(f"P {p}")