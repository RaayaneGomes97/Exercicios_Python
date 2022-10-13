# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Informe um número inteiro: '))

print('-' * 30)

for x in range(1,11):
  print('{:.0f} x {} = {:.0f}'.format(num, x,  num*x ))  

#:.0f Remover casas decimais
#:.0f Limitar a duas casas decimais

print('-' * 30) #-----------
