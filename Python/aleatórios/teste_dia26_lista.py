#Exemplo 1 lista dos caracteres
Lex1 = list("Alô Mundo")
print(Lex1)
Lex1[0] = "a"
print(Lex1)
s_ex1 = "".join(Lex1)
print(s_ex1)

print("\n")

#exemplo 2 lista de frutas
frutas_ex2 = "abacates", 'tomate', "Laranja", "Banana"
print(frutas_ex2[0])
print(frutas_ex2[1])
print(frutas_ex2[2])
print(frutas_ex2[3])

print("\n")

#exemplo 3 verifica parte das strings
nomeex3 = "João da Silva"
print(nomeex3.startswith("João"))
print(nomeex3.startswith("joão"))
print(nomeex3.endswith("Silva"))

print("\n")

#exemolo 4 retornar a string em letras maiúsculas ou minúsculas
s_ex4 = "O Rato roeu a roupa do Rei de Roma"
print(s_ex4.lower())
print(s_ex4.upper())
print(s_ex4.lower().startswith("o rato"))
print(s_ex4.upper().startswith("O RATO"))

print("\n")

#exemplo 5 verifica se há uma string dentro de outra string
s_ex5 = "Maria Amélia Souza"
print("Amélia" in s_ex5)
print("Maria" in s_ex5)
print("Souza" in s_ex5)
print("a A" in s_ex5)
print("amélia" in s_ex5)

print("\n")

#exemplo 6 verifica se não há uma string dentro de outra string
s_ex6 = "Todos os caminhos levam a Roma"
print("levam" not in s_ex6)
print("Caminhos" not in s_ex6)
print("AS" not in s_ex6)

print("\n")

#exemplo 7 conta quantas vezes algo apareceu na variável 
t_ex7 = "um tigre, dois tigres, três tigres"
print(t_ex7.count("tigre"))
print(t_ex7.count("tigres"))
print(t_ex7.count("t"))
print(t_ex7.count("z"))

print("\n")

#exemplo 8 localizar uma string dentro de outra string e falar em que ponto da outra string está a string
s_ex8 = "Alô mundo"
print(s_ex8.find("mun"))
print(s_ex8.find("ok"))

print("\n")

#exemplo 9 trocando letras numa string 
s_ex9 = "um tigre, dois tigres, três tigres"
print(s_ex9.replace("tigre", "gato"))

print("\n")

#exemplo 10 retirando espaços no começo e no fim da string
t_ex10 = "          Olá          "
print(t_ex10.strip())