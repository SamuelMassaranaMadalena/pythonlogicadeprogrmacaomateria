#Entrada
sal = float(input("Qual é o salário atual?"))
cent = float(input("Qual é a porcentagem de aumento?"))
aumentsal = float(round(sal*cent/100,2))

#Saída
print(f"O salário teve um aumento de R${aumentsal}")
print (f'O novo salário tem o valor de R${sal + aumentsal}')
