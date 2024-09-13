#Entrada
#Quantidade de cigarro fumados por dia
QntCigD = int(input("Quantos cigarros você fuma por dia? "))
#Quantidade de anos 
AFm = float(input("Há quantos anos você fuma? "))
#Tempo perdido por dia
TpPrdPrD = QntCigD * 10

if AFm == 0:
    #Tempo em dias fumando
    TpDFm = int(input("Há quantos dias você fuma"))
    print(f'Você perdeu {((TpPrdPrD * TpDFm)/ 1440):.2f} dias de vida!')
else:
    print(f"Você perdeu {(TpPrdPrD * (AFm * 365)/1440):.2f} dias de vida!")
