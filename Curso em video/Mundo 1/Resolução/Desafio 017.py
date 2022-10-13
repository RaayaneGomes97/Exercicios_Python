# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

from math import hypot #Importando apenas a função hypot
print(' [Teorema de Pitagotas] \n') 
print(' Insira os dados abaixo: \n')

print('-'*30) # Organizando o código, apenas.

adj = float(input('Cateto adjacente: ')) # adj = cateto adjacente
op  = float(input('Cateto oposto: '))    # op  = cateto oposto
hip = math.hypot(adj,op)

print('-'*30) # Organizando o código, apenas.


#{:.2f} Limitar o float a duas casas decimais.
print('\nO valor da hiptenusa é {:.2f}'.format(hip))
# Função math.hypot retorna o a hipotenusa
