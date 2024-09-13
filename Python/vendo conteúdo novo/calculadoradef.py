from os import system
def soma(a, b):
    return(a + b)
def mult(a, b):
    return(a * b)
def subt(a, b):
    return(a - b)
def divi (a, b):
    if b != 0:
        return(a / b)
    else:
        return("Erro: Divisão por zero!")

def calculadora():
    for digito in range(100000000000000000000000000000000000000000000000000000):
        print("Calculadora")
        print('digite "x" par sair da calculadora')
        digito = str(input("Digite um número: "))
        op = str(input("Digite uma operação \n+ - * /\n"))
        digito2 = str(input("Digite um número: "))
        if op == "x" or digito == "x" or digito2 == "x" or op == "X" or digito == "X" or digito2 == "X":
            break
        digito = int(digito)
        digito2 = int(digito2)
        if op == "+":
            print(f"A soma dos valores é igual a {soma(digito, digito2)}")
        elif op == "-":
            print(f'A subtração dos valores é igual a {subt(digito,digito2)}')
        elif op == "*":
            print(f"A multiplicação dos valores é igual a {mult(digito, digito2)}")
        elif op == "/":
            print(f'A divisão desse valores é igual a {divi(digito, digito2)}')
        else: 
            print("operação inválida")
        system("pause")
        system("cls")
calculadora()

def calculadora2():
    digito = str(0)
    digito2 = str(0)
    op = str(0)
    while digito != "x" or digito != "x" or digito2 != "x" or digito2 != "x" or op != "x" or op != "x":
        print('Calculadora: \nDigite "x" para sair')
        digito = str(input("Digite um número: "))
        digito2 = str(input("Digite um número: "))
        op = str(input("Digite uma operação: \n+ - * / \n"))
        if digito == "x" or digito == "x" or digito2 == "x" or digito2 == "x" or op == "x" or op == "x":
            break
        digito = int(digito)
        digito2 = int(digito2)
        if op == "+":
            print(f"A soma dos valores é igual a {soma(digito, digito2)}")
        elif op == "-":
            print(f'A subtração dos valores é igual a {subt(digito,digito2)}')
        elif op == "*":
            print(f"A multiplicação dos valores é igual a {mult(digito, digito2)}")
        elif op == "/":
            print(f'A divisão desse valores é igual a {divi(digito, digito2)}')
        else: 
            print("operação inválida")
        system("pause")
        system("cls")
calculadora2()