# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Informe um número inteiro: '))

print('-' * 30)

for x in range(1,11):
  print('{} x {:2} = {}'.format(num, x,  num*x ))  


print('-' * 30) #-----------
