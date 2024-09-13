def pares(x):
    return (x % 2 == 0)
som = 0
for a in range(100):
    if pares(a):
        if a == 0:
            som = a
        elif a != 0:
            j = a
            som = som + j
print(som)
