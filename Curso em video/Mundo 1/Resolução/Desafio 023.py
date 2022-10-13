# 23 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = str(input('Digite um número: '))

unidade = num[3]
dezena  = num[2]
centena = num[1]
milhar  = num[0]

print('Unidade: {}' .format(unidade))
print('Dezena:  {}' .format(dezena))
print('Centena: {}' .format(centena))
print('Milhar:  {}' .format(milhar))
