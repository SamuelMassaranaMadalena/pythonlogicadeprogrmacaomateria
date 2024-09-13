#Velocidade do carro
VCar = int(input("Qual a velocidade do veículo? : "))
if VCar > 80:
    Multa = float((VCar - 80) * 5)
    Multa = str(Multa).replace(".",",")
    print(f'Usuário foi multado em R$ {Multa}!')
else:
    print("Usuário dentro dos padrões")
