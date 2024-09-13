from random import randint, random
x = 0
vetor = [] #vetor vazio que terá elementos inseridos durante o programa 
while x < 10:
    vetor.append(round((randint(-100, 100)) + (random()), 2)) # soma arrendondada de valores aleatórios
    x += 1
print(f'A sequência original era: \n {vetor}')
print(f'A sequência invertida é: \n {list(reversed(vetor))}') # exibição do vetor invertido