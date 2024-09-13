def media_conceito(a):
    if a <= 4.9:
        return "D"
    elif a > 4.9 and a <= 6.9:
        return "C"
    elif a > 6.9 and a <= 8.9:
        return "B"
    else:
        return "A"
media = str(input("Insira a média do aluno: ")).replace(",",".")
media = float(media)
media = media_conceito(media)
print(media)
