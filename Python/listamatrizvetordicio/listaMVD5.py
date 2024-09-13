from random import randint, choice
seq1 = [0,0,0,0,0,0,0] #sequência 1 com os valores a serem trocados durante o programa
seq2 = [0,0,0,0,0,0,0] #sequência 2 com os valores a serem trocados durante o programa
x = 0
while x < 7: #repetição que troca os valores dos elementos do 1° vetor
    seq1[x] = randint(-1000, 1000) #gera um valor inteiro aleatório entre -1000 e 1000
    x += 1
x=0 # resetando a variável para 0
print(f"Lista 1: \n{seq1}") # exibição do primeiro vetor
while x <7: #repetição para trocar os valores dos elementos do outro vetor
    seq2[x] = randint(-100, 100)#gera um valor inteiro aleatório entre -100 e 100
    x += 1 
print(f'Lista 2: \n{seq2}') # exibição do outro vetor
seq1.extend(seq2)
print(f'List nova (depois da junção): \n{seq1}') # junção das duas listas