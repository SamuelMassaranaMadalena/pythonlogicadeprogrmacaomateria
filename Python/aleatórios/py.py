'''notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input("Nota %d: " % x))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1
print(f"Média: {soma/x}")
'''
"""numeros = [0,0,0,0,0]
x=0
while x < 5:
    numeros[x] = int(input(f"Número {x+1}: "))
    x += 1 
while True:
    escolhido = int(input("que posição você quer imprimir (0 para sair)"))
    if escolhido == 0:
        break
    print(f"Você escolheu o número {numeros[escolhido - 1]}")
"""
"""L = [1,2,3,4,5]
V = L
print(L)
print(V[0:])
V[0] = 6
print(L)
print(V)"""
"""
L = {"wow": 1945, "p": 1}
print(L.values())
print(L.keys())"""
'''tabela = {"Alface":0.45, "Batata":1.20, "Tomate":2.30, "Feijão": 1.50}
while True:
    produto = input("digite o nome do produto, fim para encerrar: ")
    if produto == "fim" or produto == "FIM":
        break
    if produto in tabela:
        print(f'Preço: {tabela[produto]:5.2f}')
    else: print("Produto não encontrado")'''

l = [1,2,5, 3,4]
l.sort(reverse=True)
print(l)