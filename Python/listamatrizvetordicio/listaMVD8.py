id = []
al = []
for x in range(5): #repete cinco vezes a atribuição dos elementos pra dentro do vetor
    id.append(input("\nDigite idade: "))
    al.append(input("Digite altura: "))
print(f"Idade: {list(reversed(id))}") #reverte a sequência 
print(f"Altura: {list(reversed(al))}")