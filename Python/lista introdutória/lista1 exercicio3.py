#Entrada
d = int(input("Quantidade de dias do Usuário: "))
h = int(input("Quantidade de horas do Usuário: "))
m = int(input("Quantidade de minutos do Usuário: "))
s = int(input("Quantidade de segundos do Usuário: "))
S = int((((d * 24)+ h)*60 + m)*60 +s)

#Saída
print(f"O usuário tem o tempo em segundos de {S}segundos")
