#Entrada
prcmerc = float(input("Qual é o preço da mercadoria?"))
desc = float(input("quanto porcento de desconto será aplicado nesse preço?"))
prcnv = float(round(prcmerc*desc/100, 2))

#Saida
print(f'O valor do desconto é de R${prcnv} e o valor a ser pago será de R${round(prcmerc - prcnv,2)}')
