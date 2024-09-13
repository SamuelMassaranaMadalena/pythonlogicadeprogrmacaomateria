num1 = int(input("digite um número inteiro: "))
num2 = int(input("digite outro número inteiro: "))
op = str(input("digite uma das operações a segur: \n+  -  /  * \n"))
while op != "+" and op != '-' and op != "*" and op != '/':
    op = str(input("digite uma das operações a segur: \n+  -  /  * \n"))

match op:
    case "+":
        print(f"A soma dos valores digitados ({num1} e {num2}) é {num1 + num2}")
    case "-":
        print(f'A subtração dos valores digitados ({num1} e {num2}) é {num1 - num2}')
    case "*":
        print(f'A multiplicação dos valores digitados ({num1} e {num2}) é {num1 * num2}')
    case "/":
        if num2 == 0:
            print("não é possível dividir por zero!")
        else:
            print(f'A divisão entre os valores digitados ({num1} e {num2}) é {num1 / num2}')
    case _:
        print(f'ERRO! Um erro inesperado aconteceu, pedimos desculpas.')
 