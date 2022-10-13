# 008 - Esreva um programa que leia um valor em metros e a exiba conertido em centímetros
# Código foi aprimorado para receber conversão para outras unidades de medida.

m = float(input('Uma distancia em metros: '))

#Trabalhando na conversão dos dados
km  = m/1000   # Quilometro
hm  = m/100    # Hectometro
dam = m/10     # Decametro
dm  = m * 10   # Decímetro
cm  = m * 100  # centimetro
mm  = m * 1000 # milimetro

print('-' * 30) #decorando o código colocando tracinhos -----

print("{} km".format(km))  #:.0f = Sem casas decimais
print("{} hm".format(hm))
print("{} dam".format(dam))
print("{} dm".format(dm))
print("{} cm".format(cm))
print("{} mm" .format(cm))

print('-' * 30) #decorando o código colocando tracinhos -----
