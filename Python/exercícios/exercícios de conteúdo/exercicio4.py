vdc = float(input("Informe o valor de venda da casa desejada: "))
vds = float(input("Informe o valor do seu salário: "))
aap = int(input("Em quantos anos você vai pagar o empréstimo bancário? "))

vprst = vdc/(aap * 12)
if vprst > vds * 0.3:
    print("Não é possível fazer o empréstimo, pois a prestação ultrapassa o valor permitido para seu salário")
else:
    print(f"Empréstimo aprovado! O valor de cada prestação é de {round(vprst, 2)}, \nse ela fosse maior que 30% do seu salário(R${vds * 0.3}) ele não seria aprovada")
