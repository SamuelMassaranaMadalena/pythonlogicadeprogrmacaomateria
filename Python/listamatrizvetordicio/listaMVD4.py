from random import choice
x = 0
seq = ['','','','','','','','','','']
while x < 10:
    #escolhe letras aleatórias do alfabeto
    seq[x] = choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    x += 1
print(seq)
soma = seq.count('a')  #soma a quantidade de vogais dentro do vetor 
soma = soma + seq.count('i')
soma = soma + seq.count('e')
soma = soma + seq.count('o')
soma = soma + seq.count('u')
print(f"há um total de {10 -soma} consoantes")