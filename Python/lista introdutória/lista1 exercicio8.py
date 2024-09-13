#Entrada
#aluguel quilometro
algkm = float(input("Quantos quilometros foram percorridos desde que o carro foi alugado? "))
#aluguel dia
algd = int(input("Por quantos dias ele foi alugado? "))
#Mostra o valor do preço arredondado em duas casas decimais
print(f"O preço a pagar sera de R${(algkm*0.15)+(algd*60):.2f}")
