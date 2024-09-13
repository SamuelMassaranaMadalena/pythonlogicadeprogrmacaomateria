from random import randint
x = 0
vetor = [] #vetor que receberá elementos durante o programa
while x < 5:
    vetor.append(randint(-100, 100)) # o novo elemento do vetor é um valor inteiro aleatório entre -100 e 100
    x += 1
print (vetor)