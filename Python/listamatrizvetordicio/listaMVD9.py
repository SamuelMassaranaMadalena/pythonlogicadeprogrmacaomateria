nota = []
soma = 0 #variável que soma os valores para fazer a média, ela também será usada para somar a quantidade de alunos que tiraram 7 ou mais na média
for x in range(10):     #repetição para receber os valores das notas
    print(F'\n{x + 1}° Aluno:')
    for b in range (4):
        media = float(input(f"Digite a {b + 1}° nota: "))
        soma += media
        b += 1
    nota.append(soma / 4) #inserindo um valor 
    soma = 0 #resetando o valor da variável
x = 0 
for x in range(10):
    if nota[x] >= 7:
        soma +=1
    x += 1
if soma == 1: #condição para escrever de forma correta se for plural ou singular
    print(f'{soma} aluno tirou 7,0 ou mais na média')
else:
    print(f'{soma} alunos tiraram 7,0 ou mais na média')