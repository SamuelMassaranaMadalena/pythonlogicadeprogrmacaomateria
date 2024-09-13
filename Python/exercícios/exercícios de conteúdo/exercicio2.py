Sal = float(input("Informe o salário do funcionário: "))
if Sal > 1250.00:
    sal = round((Sal * 1.1), 2)
    sal = str(sal).replace(".",",")
    print(f"Haverá um aumento de 10% desse salário, o novo valor dele será de: R${sal}")
else:
    sal = round((Sal * 1.15),2)
    sal = str(sal).replace(".",",")
    print(f"Haverá um aumento de 15% desse salário, o novo valor dele será de: R${sal}")

