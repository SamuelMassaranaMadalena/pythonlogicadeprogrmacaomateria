print("Escolha dois valores e um operador entre esses: +  -  *  /")
num1 = float(input("Digite um valor: "))
op = str(input("Digite o operador desejado: "))
num2 = float(input("Digite mais um valor: "))
if op == "+":
    print(f"O valor da soma desses valores é {num1 + num2}")
elif op == "-":
    print(f"O valor da subtração desses valores é {num1 - num2}")
elif op == "*":
    print(f'O valor da multiplicação desses valores é {num1 * num2}')
elif op == "/":
    print(f'O valor da divisão desses valores é {num1/num2}')
else:
    print("Operação inválida, execute novamente o arquivo e escolha uma operação entre essas: +  -  *  /")
