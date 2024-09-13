def fahrenheit(a):
    return ((9*a/5) + 32)
def celcius(a):
    return (5*(a-32)/9)
graus = str(input("Escolha uma grandeza de medida de temperatura entre °C e °F \n:"))
temp = str(input("Agora escolha a temperatura que deseja converter\n:"))
temp = str(temp).replace(",",".")
temp = float(temp)
if graus == "C" or graus == "°C" or graus == "c" or graus == "°c":
    temp = fahrenheit(temp)
    temp = str(temp).replace(".",",")
    print(f"O valor da conversão de graus celcius para graus fahrenheit é {temp}")
else:
    temp = celcius(temp)
    temp = str(temp).replace(".",",")
    print(f"O valor da conversão de graus fahrenheit para graus celcius é {temp}")