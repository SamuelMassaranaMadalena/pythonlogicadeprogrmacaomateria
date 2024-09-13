def mediavetor(a,b): #função que faz a média de um vetor. "a" é a variável que tem o vetor e "b" é a quantidade de elementos que existem dentro do vetor
    soma = 0
    med = 0
    while med < b:  #se b for maior a função não funciona
        X = a[med]
        soma = soma + X
        med = med + 1
    return (soma/med)
T = [-10, -8, 0, 1, 2, 5, -2, -4]
print(f"O menor valor é: {min(T[0:])}") #função mostra o menor valor
print(f"O maior valor é: {max(T[0:])}") #função mostra o maior valor
print(f"A média dos valores é: {mediavetor(T, 8)}")