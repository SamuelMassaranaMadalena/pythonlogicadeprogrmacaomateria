notas = [0,0,0,0] #vetor com valores a serem trocados durante o programa
x = 0
soma = 0
while x < 4: #repetição que troca os valores dos elementos
    notas[x] = float(input(f"Digite a {x+1}° nota do aluno: "))
    soma += notas[x]
    if notas[x] > 10 or notas[x] < 0: #mensagem de erro caso o valor não se encaixe dentro dos valores usados para notas
        print("Nota inválida!")
        soma -= notas[x]
        del notas[x]
    else:
        print(notas[x])
        x += 1
print(f'A média do aluno é {soma / x :.2f}')  #exibição da média com duas casas decimais